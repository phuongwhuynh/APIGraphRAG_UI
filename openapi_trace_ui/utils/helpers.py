from typing import Any, Dict, List, Optional


def get_endpoints(spec: Dict) -> List[Dict]:
    paths = spec.get("paths", {})
    result = []

    for path, methods in paths.items():
        for method, data in methods.items():
            result.append({"path": path, "method": method, "data": data})

    return result


def get_summary(endpoint: Dict) -> str:
    return endpoint["data"].get("summary", "")


def get_description(endpoint: Dict) -> str:
    return endpoint["data"].get("description", "")


def get_parameters(endpoint: Dict) -> List[Dict]:
    return endpoint["data"].get("parameters", [])


def group_parameters(params: List[Dict]) -> Dict[str, List[Dict]]:
    grouped = {"path": [], "query": [], "header": [], "cookie": []}

    for p in params:
        location = p.get("in", "query")
        grouped.setdefault(location, []).append(p)

    return grouped


def get_request_body(endpoint: Dict) -> Optional[Dict]:
    return endpoint["data"].get("requestBody")


def get_request_schema(request_body: Dict) -> Optional[Dict]:
    if not request_body:
        return None

    content = request_body.get("content", {})
    json_body = content.get("application/json", {})
    return json_body.get("schema")


def get_responses(endpoint: Dict) -> Dict:
    return endpoint["data"].get("responses", {})


def is_error_response(status_code: str) -> bool:
    return status_code.startswith("4") or status_code.startswith("5")


def split_responses(responses: Dict) -> Dict[str, List]:
    success = []
    errors = []

    for code, res in responses.items():
        if is_error_response(code):
            errors.append((code, res))
        else:
            success.append((code, res))

    return {"success": success, "errors": errors}


def get_schema_from_response(response: Dict) -> Optional[Dict]:
    content = response.get("content", {})
    json_body = content.get("application/json", {})
    return json_body.get("schema")


def get_ref_name(schema: Dict) -> Optional[str]:
    ref = schema.get("$ref")
    if not ref:
        return None
    return ref.split("/")[-1]


def resolve_ref(spec: Dict, ref: str) -> Optional[Dict]:
    parts = ref.strip("#/").split("/")
    current = spec

    for part in parts:
        current = current.get(part, {})
    return current


def get_trace(obj: Dict) -> Optional[Dict]:
    trace = obj.get("x-trace")
    if not trace:
        return None
    # Only return trace if it has start_line/end_line or line
    if ("start_line" in trace and "end_line" in trace) or ("line" in trace):
        return trace
    return None


def has_trace(obj: Dict) -> bool:
    trace = obj.get("x-trace")
    if not trace:
        return False
    return ("start_line" in trace and "end_line" in trace) or ("line" in trace)


def format_trace(trace: Dict) -> str:
    if not trace:
        return ""

    file = trace.get("file", "")
    func = trace.get("function", "")
    start_line = trace.get("start_line")
    end_line = trace.get("end_line")
    line = trace.get("line")

    if start_line is not None and end_line is not None:
        return f"{file}::{func} ({start_line}-{end_line})"
    elif line is not None:
        return f"{file}::{func} (line {line})"
    return f"{file}::{func}"


def get_schema_properties(schema: Dict) -> Dict:
    return schema.get("properties", {})


def is_array(schema: Dict) -> bool:
    return schema.get("type") == "array"


def get_array_items(schema: Dict) -> Optional[Dict]:
    return schema.get("items")


def get_components(spec: Dict) -> Dict:
    return spec.get("components", {})


def get_schemas(spec: Dict) -> Dict:
    return spec.get("components", {}).get("schemas", {})


def group_endpoints_by_tag(spec: Dict) -> Dict[str, List[Dict]]:
    """Group endpoints by their first tag (or 'default' if none). Returns dict tag -> [endpoint]."""
    groups: Dict[str, List[Dict]] = {}
    for ep in get_endpoints(spec):
        tags = ep.get("data", {}).get("tags") or ["default"]
        for tag in tags:
            groups.setdefault(tag, []).append(ep)
    return groups
