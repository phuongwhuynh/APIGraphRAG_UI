run-ui:
	poetry run uvicorn openapi_trace_ui.server:app --reload