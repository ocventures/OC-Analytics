from models import Event, Session

def save_event(user_id, event_type, event_data):
    session = Session()
    event = Event(user_id=user_id, event_type=event_type, event_data=event_data)
    session.add(event)
    session.commit()
    session.close()

def get_events(user_id=None):
    session = Session()
    query = session.query(Event)
    if user_id:
        query = query.filter_by(user_id=user_id)
    events = query.all()
    session.close()
    return events
