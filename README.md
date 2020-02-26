# Endpoints
## localhost:8080/calc/
Calculate an expression.
- Input: {"expression": "x+t*y", "variables": {"x": 10, "y": 1, "t": 11}}
- Output: {"expression_id": 1}
## localhost:8080/result/
Get a result.
- Input: {"id": 1}
- Output: {"result": 21.0}