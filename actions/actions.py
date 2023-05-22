# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from core import predict
from core import ad
ner_bert = predict.NER_BERT()

class GetAddressAction(Action):

    def name(self) -> Text:
        return "action_get_address"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get('text')
        predict_ner = ner_bert.evaluate_one_text(user_message)
        if predict_ner:
            address = ad.search_address(predict_ner)
            print(address)
            if len(address)> 1:
                kq = f"Sau đây một số địa chỉ tôi tìm được từ {predict_ner} \n"
                kq +='\n'.join([' - '+i[0] for i in address])
                kq += '\n' + 'Bạn vui lòng chọn địa chỉ với cú pháp: Tôi muốn tìm bất động sản xung quanh [Địa Chỉ]:'
                dispatcher.utter_message(text=kq)
            elif len(address)== 1:
                kq = f"Sau đây là một số bất động sản xung quanh {address[0][0]}"
                dispatcher.utter_message(text=f"Sau đây là một số bất động sản xung quanh {address[0][0]}{ad.bds_demo()}")
        else:
            dispatcher.utter_message(text='Bạn vui lòng chọn địa chỉ với cú pháp: Tôi muốn tìm bất động sản: [Địa Chỉ]')
        return []