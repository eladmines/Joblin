class Job:
    def __init__(self, title, location, description, qualifications, date, link, company, image, id):
        self.title = title
        self.location = location
        self.description = description
        self.qualifications = qualifications
        self.date = date
        self.link = link
        self.company = company
        self.image = image
        self.id = id

    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title

    def get_location(self):
        return self.location
    
    def set_location(self, location):
        self.location = location

    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description

    def get_qualifications(self):
        return self.qualifications
    
    def set_qualifications(self, qualifications):
        self.qualifications = qualifications

    def get_date(self):
        return self.date
    
    def set_date(self, date):
        self.date = date

    def get_link(self):
        return self.link
    
    def set_link(self, link):
        self.link = link

    def get_company(self):
        return self.company
    
    def set_company(self, company):
        self.company = company

    def get_image(self):
        return self.image
    
    def set_image(self, image):
        self.image = image

    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id
        
    def __str__(self):
        return (f"Job(id={self.id}, title={self.title}, location={self.location}, "
                f"description={self.description}, qualifications={self.qualifications}, "
                f"date={self.date}, link={self.link}, company={self.company}, image={self.image})")
