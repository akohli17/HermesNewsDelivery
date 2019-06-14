import sys
sys.path.append('/Users/matteorusso/Desktop/cos-333-project-dynamic-news-delivery/secure_login_app/finish/')
from dnd import db
from dnd.models import Interest
Interest.__table__.drop(db.session.bind)
Interest.__table__.create(db.session.bind)
db.session.commit()