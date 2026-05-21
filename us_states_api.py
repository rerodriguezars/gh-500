"""
US States API - Returns information about US states
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# US States data
US_STATES = [
    {"code": "AL", "name": "Alabama"},
    {"code": "AK", "name": "Alaska"},
    {"code": "AZ", "name": "Arizona"},
    {"code": "AR", "name": "Arkansas"},
    {"code": "CA", "name": "California"},
    {"code": "CO", "name": "Colorado"},
    {"code": "CT", "name": "Connecticut"},
    {"code": "DE", "name": "Delaware"},
    {"code": "FL", "name": "Florida"},
    {"code": "GA", "name": "Georgia"},
    {"code": "HI", "name": "Hawaii"},
    {"code": "ID", "name": "Idaho"},
    {"code": "IL", "name": "Illinois"},
    {"code": "IN", "name": "Indiana"},
    {"code": "IA", "name": "Iowa"},
    {"code": "KS", "name": "Kansas"},
    {"code": "KY", "name": "Kentucky"},
    {"code": "LA", "name": "Louisiana"},
    {"code": "ME", "name": "Maine"},
    {"code": "MD", "name": "Maryland"},
    {"code": "MA", "name": "Massachusetts"},
    {"code": "MI", "name": "Michigan"},
    {"code": "MN", "name": "Minnesota"},
    {"code": "MS", "name": "Mississippi"},
    {"code": "MO", "name": "Missouri"},
    {"code": "MT", "name": "Montana"},
    {"code": "NE", "name": "Nebraska"},
    {"code": "NV", "name": "Nevada"},
    {"code": "NH", "name": "New Hampshire"},
    {"code": "NJ", "name": "New Jersey"},
    {"code": "NM", "name": "New Mexico"},
    {"code": "NY", "name": "New York"},
    {"code": "NC", "name": "North Carolina"},
    {"code": "ND", "name": "North Dakota"},
    {"code": "OH", "name": "Ohio"},
    {"code": "OK", "name": "Oklahoma"},
    {"code": "OR", "name": "Oregon"},
    {"code": "PA", "name": "Pennsylvania"},
    {"code": "RI", "name": "Rhode Island"},
    {"code": "SC", "name": "South Carolina"},
    {"code": "SD", "name": "South Dakota"},
    {"code": "TN", "name": "Tennessee"},
    {"code": "TX", "name": "Texas"},
    {"code": "UT", "name": "Utah"},
    {"code": "VT", "name": "Vermont"},
    {"code": "VA", "name": "Virginia"},
    {"code": "WA", "name": "Washington"},
    {"code": "WV", "name": "West Virginia"},
    {"code": "WI", "name": "Wisconsin"},
    {"code": "WY", "name": "Wyoming"},
]


@app.route("/api/states", methods=["GET"])
def get_all_states():
    """Get all US states"""
    return jsonify({
        "success": True,
        "count": len(US_STATES),
        "data": US_STATES
    })


@app.route("/api/states/<state_code>", methods=["GET"])
def get_state_by_code(state_code):
    """Get a specific state by state code"""
    state_code = state_code.upper()
    state = next((s for s in US_STATES if s["code"] == state_code), None)
    
    if state is None:
        return jsonify({
            "success": False,
            "error": f"State with code '{state_code}' not found"
        }), 404
    
    return jsonify({
        "success": True,
        "data": state
    })


@app.route("/api/states/name/<state_name>", methods=["GET"])
def get_state_by_name(state_name):
    """Get a specific state by state name"""
    state_name_lower = state_name.lower()
    state = next((s for s in US_STATES if s["name"].lower() == state_name_lower), None)
    
    if state is None:
        return jsonify({
            "success": False,
            "error": f"State with name '{state_name}' not found"
        }), 404
    
    return jsonify({
        "success": True,
        "data": state
    })


@app.route("/api/states/search", methods=["GET"])
def search_states():
    """Search states by query parameter"""
    query = request.args.get("q", "").lower()
    
    if not query:
        return jsonify({
            "success": False,
            "error": "Query parameter 'q' is required"
        }), 400
    
    results = [s for s in US_STATES if query in s["name"].lower() or query in s["code"].lower()]
    
    return jsonify({
        "success": True,
        "count": len(results),
        "data": results
    })


@app.route("/api/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "US States API"
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
