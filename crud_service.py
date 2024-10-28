from sqlalchemy.orm import Session
from typing import List

import models, schemas

# auto generated route, get a record
def get_persons_by_rollnumber(db: Session, rollnumber: int):
      persons_one = db.query(models.Persons).filter(models.Persons.rollnumber == rollnumber).first()
      res = {
        'dsads': persons_one,
        'finaloutput': persons_one,
      }
      return res

def create_persons(db: Session, rollnumber: str, fullname: str, age: str, profession: str):
      record_to_be_added = {'rollnumber': rollnumber, 'fullname': fullname, 'age': age, 'profession': profession}
      new_persons = models.Persons(**record_to_be_added)
      db.add(new_persons)
      db.commit()
      persons_inserted_record = new_persons
      return persons_inserted_record

def update_persons_by_rollnumber(db: Session, rollnumber: str, fullname: str, age: str, profession: str):
      record_to_update = db.query(models.Persons).filter(models.Persons.rollnumber == rollnumber).first()
      for key, value in {'rollnumber': rollnumber, 'fullname': fullname, 'age': age, 'profession': profession}.items():
          setattr(record_to_update, key, value)
      db.commit()
      db.refresh(record_to_update)
      persons_edited_record = record_to_update

      return persons_edited_record

def delete_persons_by_rollnumber(db: Session, rollnumber: int):
      persons_deleted = None
      record_to_delete = db.query(models.Persons).filter(models.Persons.rollnumber == rollnumber).first()

      if record_to_delete:
          db.delete(record_to_delete)
          db.commit()
          persons_deleted = record_to_delete
      res = {
      }
      return res

def get_all_addresses(db: Session):
      addresses_all = db.query(models.Addresses).all()
      return addresses_all

# auto generated route, get a record
def get_addresses_by_id(db: Session, id: int):
      addresses_one = db.query(models.Addresses).filter(models.Addresses.id == id).first()
      return addresses_one

def create_addresses(db: Session, id: str, street: str, city: str, state: str, country: str, postal_code: str, created_at: str, updated_at: str):
      record_to_be_added = {'id': id, 'street': street, 'city': city, 'state': state, 'country': country, 'postal_code': postal_code, 'created_at': created_at, 'updated_at': updated_at}
      new_addresses = models.Addresses(**record_to_be_added)
      db.add(new_addresses)
      db.commit()
      addresses_inserted_record = new_addresses
      return addresses_inserted_record

def update_addresses_by_id(db: Session, id: str, street: str, city: str, state: str, country: str, postal_code: str, created_at: str, updated_at: str):
      record_to_update = db.query(models.Addresses).filter(models.Addresses.id == id).first()
      for key, value in {'id': id, 'street': street, 'city': city, 'state': state, 'country': country, 'postal_code': postal_code, 'created_at': created_at, 'updated_at': updated_at}.items():
          setattr(record_to_update, key, value)
      db.commit()
      db.refresh(record_to_update)
      addresses_edited_record = record_to_update

      res = {
      }
      return res

def delete_addresses_by_id(db: Session, id: int):
      addresses_deleted = None
      record_to_delete = db.query(models.Addresses).filter(models.Addresses.id == id).first()

      if record_to_delete:
          db.delete(record_to_delete)
          db.commit()
          addresses_deleted = record_to_delete
      return addresses_deleted

