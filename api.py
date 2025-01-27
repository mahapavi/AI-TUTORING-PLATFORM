@app.route('/api/recommend/<int:user_id>', methods=['GET'])
def personalized_recommend(user_id):
    recs = recommend(user_id)
    return jsonify({"recommendations": recs}), 200
