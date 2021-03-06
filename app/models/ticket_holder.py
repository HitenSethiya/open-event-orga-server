import base64
from StringIO import StringIO

import qrcode

from . import db


class TicketHolder(db.Model):
    __tablename__ = "ticket_holders"

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    email = db.Column(db.String)
    job_title = db.Column(db.String)
    phone_no = db.Column(db.Integer)
    work_phone = db.Column(db.Integer)
    mobile_phone = db.Column(db.Integer)
    tax_business_info = db.Column(db.String)
    # billing_address = db.Column(db.String)
    work_address = db.Column(db.String)
    shipping_address = db.Column(db.String)
    home_address = db.Column(db.String)
    organisation = db.Column(db.String)
    website = db.Column(db.String)
    blog = db.Column(db.String)
    twitter = db.Column(db.String)
    facebook = db.Column(db.String)
    git_repo = db.Column(db.String)
    gender = db.Column(db.String)
    dob = db.Column(db.DateTime)
    address = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    country = db.Column(db.String)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id', ondelete='CASCADE'))
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id', ondelete='CASCADE'))
    order = db.relationship('Order', backref='ticket_holders')
    ticket = db.relationship('Ticket', backref='ticket_holders')
    checked_in = db.Column(db.Boolean, default=False)

    def __init__(self,
                 firstname=None,
                 lastname=None,
                 email=None,
                 address=None,
                 city=None,
                 state=None,
                 country=None,
                 ticket_id=None,
                 checked_in=False,
                 order_id=None,
                 job_title=None,
                 phone_no=None,
                 work_phone=None,
                 mobile_phone=None,
                 tax_business_info=None,
                 # billing_address = None,
                 work_address=None,
                 shipping_address=None,
                 home_address=None,
                 organisation=None,
                 website=None,
                 blog=None,
                 twitter=None,
                 facebook=None,
                 git_repo=None,
                 gender=None,
                 dob=None
                 ):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.job_title = job_title
        self.phone_no = phone_no
        self.work_phone = work_phone
        self.mobile_phone = mobile_phone
        self.tax_business_info = tax_business_info
        # self.billing_address = billing_address
        self.work_address = work_address
        self.shipping_address = shipping_address
        self.home_address = home_address
        self.organisation = organisation
        self.website = website
        self.blog = blog
        self.twitter = twitter
        self.facebook = facebook
        self.git_repo = git_repo
        self.gender = gender
        self.dob = dob
        self.city = city
        self.address = address
        self.state = state
        self.ticket_id = ticket_id
        self.country = country
        self.order_id = order_id
        self.checked_in = checked_in

    def __repr__(self):
        return '<TicketHolder %r>' % self.id

    def __str__(self):
        return '<TicketHolder %r>' % self.id

    def __unicode__(self):
        return '<TicketHolder %r>' % self.id

    @property
    def name(self):
        firstname = self.firstname if self.firstname else ''
        lastname = self.lastname if self.lastname else ''
        if firstname and lastname:
            return u'{} {}'.format(firstname, lastname)
        else:
            return ''

    @property
    def qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=0,
        )
        qr.add_data(self.order.identifier + "/" + str(self.id))
        qr.make(fit=True)
        img = qr.make_image()

        buffer = StringIO()
        img.save(buffer, format="JPEG")
        img_str = base64.b64encode(buffer.getvalue())
        return img_str

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {'id': self.id,
                'firstname': self.firstname,
                'lastname': self.lastname,
                'email': self.email,
                'city': self.city,
                'address': self.address,
                'state': self.state,
                'country': self.country,
                'job_title': self.job_title,
                'phone_no': self.phone_no,
                'work_phone': self.work_phone,
                'mobile_phone': self.mobile_phone,
                'tax_business_info': self.tax_business_info,
                'billing_address': self.billing_address,
                'work_address': self.work_address,
                'shipping_address': self.shipping_address,
                'home_address': self.home_address,
                'organisation': self.organisation,
                'website': self.website,
                'blog': self.blog,
                'twitter': self.twitter,
                'facebook': self.facebook,
                'git_repo': self.git_repo,
                'gender': self.gender,
                'dob': self.dob,

                }
