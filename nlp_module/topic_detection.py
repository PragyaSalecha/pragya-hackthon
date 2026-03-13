topics = {

"delivery": ["delivery","late","shipping"],

"queue": ["queue","waiting","line"],

"product_quality": ["quality","broken","defective"],

"staff_behavior": ["staff","rude","service"]

}

def detect_topic(text):

    for topic,words in topics.items():

        for word in words:

            if word in text:
                return topic

    return "general"