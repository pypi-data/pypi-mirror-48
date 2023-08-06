__author__ = 'godq'

import json

from dagflow.loader import get_MQ_Broker_Object

mq_broker = get_MQ_Broker_Object()


class EventOperation:
    Start_Flow = "start_flow"
    Finish_Step = "finish_step"
    Waiting_Event = "waiting_event"


def add_event_to_repo(dag_name, run_id, event):
    from dagflow.loader import get_DagRepo_Object
    dag_repo = get_DagRepo_Object()
    dag_repo.add_dag_run_event(dag_name, run_id, event=event)


def send_event_message(event):
    if isinstance(event, dict):
        event = json.dumps(event)
    # message_queue.put_message(event)
    mq_broker.send_msg(event)

