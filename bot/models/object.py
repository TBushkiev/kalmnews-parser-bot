from database.base_class import Base


# no need for __tablename__ because of declarative style (database.base_class)
class Object(Base):
    pass
