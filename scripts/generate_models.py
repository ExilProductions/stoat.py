#!/usr/bin/env python3
import json
import argparse
import os
from typing import Any, List, Dict, Set, Optional


class SchemaModel:
    """Stores schema info for generation and import resolution."""

    def __init__(self, name: str, schema: dict, category: str):
        self.name = name
        self.schema = schema
        self.category = category
        self.fields: Dict[str, str] = {}
        self.docstring: Optional[str] = schema.get("description")
        self.required: Set[str] = set(schema.get("required", []))
        self.dependencies: Set[str] = set()


def json_type_to_py(json_type: str) -> str:
    mapping = {
        "string": "str",
        "integer": "int",
        "number": "float",
        "boolean": "bool",
        "object": "dict",
        "array": "list",
    }
    return mapping.get(json_type, "Any")


def generate_models_files(openapi: dict, output_dir: str):
    """Generate Pydantic models from OpenAPI JSON spec with automatic imports, deduplication, and __init__.py generation."""

    os.makedirs(output_dir, exist_ok=True)
    schemas: Dict[str, dict] = openapi.get("components", {}).get("schemas", {})
    generated: Dict[str, SchemaModel] = {}

    def resolve_ref(ref: str) -> dict:
        if not ref.startswith("#/components/schemas/"):
            raise ValueError(f"Unsupported $ref format: {ref}")
        ref_name = ref.split("/")[-1]
        return ref_name, schemas[ref_name]

    def infer_category(schema_name: str, schema: dict) -> str:
        """Use tags if available, otherwise schema name prefix."""
        if "x-tags" in schema and schema["x-tags"]:
            return schema["x-tags"][0].lower()
        name_lower = schema_name.lower()
        if name_lower.startswith("features"):
            return "features"
        elif name_lower.startswith("build"):
            return "build"
        elif name_lower.startswith("query"):
            return "query"
        return ""

    def recurse_model(name: str, schema: dict, category: str):
        """Recursively generate SchemaModel and collect dependencies."""
        if name in generated:
            return generated[name]

        description = schema.get("description")
        if "allOf" in schema and schema["allOf"]:
            allof_sub = schema["allOf"][0]
            description = allof_sub.get("description", description)
            schema = {**allof_sub, **schema}

        model = SchemaModel(name, schema, category)
        model.docstring = description
        model.required = set(schema.get("required", []))
        props = schema.get("properties", {})

        for key, prop in props.items():
            field_type = "Any"

            if "$ref" in prop:
                ref_name, ref_schema = resolve_ref(prop["$ref"])
                ref_category = infer_category(ref_name, ref_schema)
                dep_model = recurse_model(ref_name, ref_schema, ref_category)
                field_type = dep_model.name
                model.dependencies.add(dep_model.name)

            elif "allOf" in prop:
                for sub in prop["allOf"]:
                    if "$ref" in sub:
                        ref_name, ref_schema = resolve_ref(sub["$ref"])
                        ref_category = infer_category(ref_name, ref_schema)
                        dep_model = recurse_model(ref_name, ref_schema, ref_category)
                        field_type = dep_model.name
                        model.dependencies.add(dep_model.name)
                    elif sub.get("type") == "object":
                        nested_name = f"{name}{key.title()}Model"
                        dep_model = recurse_model(nested_name, sub, category)
                        field_type = dep_model.name
                        model.dependencies.add(dep_model.name)

            elif prop.get("type") == "object":
                nested_name = f"{name}{key.title()}Model"
                dep_model = recurse_model(nested_name, prop, category)
                field_type = dep_model.name
                model.dependencies.add(dep_model.name)

            elif prop.get("type") == "array":
                items = prop.get("items", {})
                if "$ref" in items:
                    ref_name, ref_schema = resolve_ref(items["$ref"])
                    ref_category = infer_category(ref_name, ref_schema)
                    dep_model = recurse_model(ref_name, ref_schema, ref_category)
                    field_type = f"List[{dep_model.name}]"
                    model.dependencies.add(dep_model.name)
                elif items.get("type") == "object":
                    nested_name = f"{name}{key.title()}ItemModel"
                    dep_model = recurse_model(nested_name, items, category)
                    field_type = f"List[{dep_model.name}]"
                    model.dependencies.add(dep_model.name)
                else:
                    field_type = f"List[{json_type_to_py(items.get('type'))}]"
            else:
                field_type = json_type_to_py(prop.get("type"))

            if key not in model.required:
                field_type = f"Optional[{field_type}]"

            model.fields[key] = field_type

        generated[name] = model
        return model

    # Step 1: Collect all models
    for schema_name, schema_def in schemas.items():
        category = infer_category(schema_name, schema_def)
        recurse_model(schema_name, schema_def, category)

    # Step 2: Write files with imports and __init__.py
    folders_written: Set[str] = set()
    for model_name, model in generated.items():
        imports = ["from typing import List, Any"]
        if any("Optional[" in t for t in model.fields.values()):
            imports[0] = "from typing import List, Any, Optional"
        imports.append("from pydantic import BaseModel")
        imports.append("")

        category_dir = os.path.join(output_dir, model.category) if model.category else output_dir
        os.makedirs(category_dir, exist_ok=True)
        file_path = os.path.join(category_dir, f"{model.name}.py")

        # Add __init__.py if not already
        if category_dir not in folders_written:
            init_path = os.path.join(category_dir, "__init__.py")
            if not os.path.exists(init_path):
                with open(init_path, "w") as f:
                    f.write("")
            folders_written.add(category_dir)

        # Dependency imports
        dep_lines = []
        for dep in model.dependencies:
            dep_model = generated[dep]
            if dep_model.category == model.category:
                dep_lines.append(f"from .{dep_model.name} import {dep_model.name}")
            else:
                rel_path = os.path.relpath(os.path.join(output_dir, dep_model.category), category_dir)
                rel_path = rel_path.replace(os.sep, ".")
                dep_lines.append(f"from {rel_path}.{dep_model.name} import {dep_model.name}")

        # Class code
        class_lines = [f"class {model.name}(BaseModel):"]
        if model.docstring:
            class_lines.append(f'    """{model.docstring}"""')
        if model.fields:
            for k, t in model.fields.items():
                class_lines.append(f"    {k}: {t}")
        else:
            class_lines.append("    pass")

        # Write file
        with open(file_path, "w") as f:
            f.write("\n".join(imports + dep_lines + [""] + class_lines))


def main():
    parser = argparse.ArgumentParser(
        description="Generate Pydantic models from OpenAPI JSON spec with deduplication, auto-imports, and __init__.py"
    )
    parser.add_argument("input", help="Path to OpenAPI JSON spec")
    parser.add_argument("output_dir", help="Output directory")
    args = parser.parse_args()

    with open(args.input, "r") as f:
        openapi = json.load(f)

    generate_models_files(openapi, args.output_dir)
    print(f"Pydantic models written to {args.output_dir}")


if __name__ == "__main__":
    main()