from flask import Flask
import boto3
 
app = Flask(__name__)
 
sns = boto3.client("sns", region_name="us-east-1")
 
TOPIC_ARN = "arn:aws:sns:us-east-1:925729917602:uwwnonprod-sns-topic"
 
@app.route("/")
def home():
    # Send SNS email
    # sns.publish(
    #     TopicArn=TOPIC_ARN,
    #     Message="LinkedIn API was triggered!",
    #     Subject="ECS Notification"
    # )
 
    return "Sample ECS deployment"
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)