import tweepy
import time
from datetime import datetime
from twitter_config import auth_conf, BEARER_TOKEN
from kafka_producer import create_producer, delivery_report
from kafka_config import TOPIC
from confluent_kafka.serialization import SerializationContext, MessageField
from logger import logging


logger = logging.getLogger(__name__)

auth = auth_conf()
api = tweepy.API(auth)

#Get data with rule

search_terms = ['bitcoin lang:en', 'btc lang:en']
producer, json_serializer = create_producer()


class MyStream(tweepy.StreamingClient):
    def _int_(self, bearer_token, wait_on_limit =False, max_retries=10):
        self.bearer_token = bearer_token
        self.wait_on_rate_limit = wait_on_limit
        self.max_retries = max_retries

    def on_connect(self):
        logger.info("Connected")

    def on_tweet(self, tweet):      
        data = {
            "id": str(tweet.id),
            "text": tweet.text,
            "created_at": datetime.now().strftime("%m/%d/%Y-%H:%M:%S")
        }
        
        producer.produce(topic=TOPIC,
                         key=str(tweet.id),
                         value=json_serializer(data, SerializationContext(TOPIC, MessageField.VALUE)),
                         on_delivery=delivery_report)
        producer.flush()
        logger.info(data)
        time.sleep(30)  # delay time by seconds

    def on_connection_error(self):
        self.disconnect()
    
    def on_exception(self, exception):
        print(exception)
        time.sleep(30)
        pass

    def on_errors(self, status):
        print(status)
        return True


stream = MyStream(bearer_token=BEARER_TOKEN)


for term in search_terms:
    stream.add_rules(tweepy.StreamRule(term))

stream.filter()
