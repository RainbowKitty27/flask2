from flask import Flask, jsonify, request
import csv
all_articles=[]

with open("articles.csv",encoding='utf-8') as f:
    reader=csv.reader(f)
    data=list(reader)
    all_articles=data[1:]
    
liked_articles=[]
unliked_articles=[]

app=Flask(__name__)

@app.route("/get-article")
def get_article():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
        
    })
    
@app.route("/liked-article", methods=["POST"])
def liked_article():
        article=all_articles[0]
        liked_articles.append(article)
        all_articles.pop(0)
        return jsonify({
            "status":"success"
    }), 201
        
@app.route("/unliked-article", methods=["POST"])
def unliked_article():
        article=all_articles[0]
        unliked_articles.append(article)
        all_articles.pop(0)
        return jsonify({
            "status":"success"
    }), 201
@app.route("/popular-article")
def popular_article():
        article_data=[]
        for article in output:
            _d={
                "url":article[0],
                "title":article[1],
                "text":article[2],
                "lang":article[3],
                "total_events":article[4]
            }
            article_data.append(_d)
        return jsonify({
            "data":article_data,
            "status":"success"
    }), 200
@app.route("/recommended-articles")
def recommended_articles():
    all_recommended=[]
    for liked_article in liked_articles:
        output=get_recommendations(liked_article[4])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended=list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    article_data=[]
    for recommended in all_recommended:
        _d={
                "url":recommended[0],
                "title":recommended[1],
                "text":recommended[2],
                "lang":recommended[3],
                "total_events":recommended[4]
            }
        article_data.append(_d)
    return jsonify({
        "data":article_data,
        "status":"success"
}), 200


if __name__=="__main__":
    app.run()
   
