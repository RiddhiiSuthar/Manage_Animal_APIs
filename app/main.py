from uuid import UUID

import models
from database import get_db
from fastapi import Depends, FastAPI, HTTPException
from schemas import cat, dog
from sqlalchemy.orm import Session
from sqlalchemy import text


app = FastAPI()


# list of cities
@app.get("/cities")
def get(db: Session = Depends(get_db)):
    all_cities = db.query(models.City).all()
    return all_cities


# Cats operations
@app.post("/cats")
def create_cat(cat: cat, db: Session = Depends(get_db)):

    new_cat = models.Cat(**cat.dict())
    db.add(new_cat)
    db.commit()
    db.refresh(new_cat)
    return {"status": "success", "note": new_cat}


@app.get("/cats")
def get_cats(db: Session = Depends(get_db)):
    all_cats = db.query(models.Cat).all()
    return all_cats


@app.put("/cats/{cat_id}")
def update_cat(cat_id: UUID, cat: cat, db: Session = Depends(get_db)):
    # Check if the provided cat_id exists in the database
    cat_in_db = db.query(models.Cat).filter(models.Cat.id == cat_id).first()
    if not cat_in_db:
        raise HTTPException(status_code=404, detail="Cat not found")

    # Update the cat's information
    cat_in_db.favorite_fish = cat.favorite_fish

    db.commit()
    db.refresh(cat_in_db)
    return {"status": "success", "note": "Cat updated successfully"}


@app.delete("/cats/{cat_id}")
def delete_cat(cat_id: UUID, db: Session = Depends(get_db)):
    # Check if the provided cat_id exists in the database
    cat = db.query(models.Cat).filter(models.Cat.id == cat_id).first()
    if not cat:
        raise HTTPException(status_code=404, detail="Cat not found")

    # Delete the cat
    db.delete(cat)
    db.commit()
    return {"status": "success", "note": "Cat deleted successfully"}


# List all cats in a city
@app.get("/city/{city_name}/cats")
def get_cats_in_city(city_name, db: Session = Depends(get_db)):
    city = db.query(models.City).filter(models.City.name == city_name).first()
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")

    cats = db.query(models.Cat).filter_by(city_id=city.id).all()

    return cats


@app.post("/city/{city_name}/cats")
def create_cats_in_city(city_name, cat: cat, db: Session = Depends(get_db)):
    city = db.query(models.City).filter(models.City.name == city_name).first()
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")

    db_cat = (
        db.query(models.Cat)
        .filter_by(favorite_fish=cat.dict().get("favorite_fish"))
        .first()
    )

    if db_cat:
        db_cat.city_id = city.id
        db.commit()
        db.refresh(db_cat)
        return db_cat
    else:
        new_cat = models.Cat(**cat.dict())
        db.add(new_cat)
        new_cat.city_id = city.id
        db.commit()
        db.refresh(new_cat)
        return new_cat


@app.put("/city/{city_name}/cats/{cat_id}")
def update_cat_in_city(
    city_name, cat_id: UUID, cat: cat, db: Session = Depends(get_db)
):
    city = db.query(models.City).filter(models.City.name == city_name).first()
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")

    db_cat = db.query(models.Cat).filter_by(id=cat_id, city_id=city.id).first()
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Cat not found in this city")

    db_cat.favorite_fish = cat.favorite_fish
    db_cat.city_id = city.id

    db.commit()
    db.refresh(db_cat)

    return db_cat


@app.delete("/city/{city_name}/cats/{cat_id}")
def delete_cat_in_city(city_name, cat_id: UUID, db: Session = Depends(get_db)):
    city = db.query(models.City).filter(models.City.name == city_name).first()
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")

    db_cat = db.query(models.Cat).filter_by(id=cat_id, city_id=city.id).first()
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Cat not found in this city")

    db.delete(db_cat)
    db.commit()

    return {"message": "Cat deleted successfully"}


# Dogs operations
@app.post("/dogs")
def create_dog(dog: dog, db: Session = Depends(get_db)):
    new_dog = models.Dog(**dog.dict())
    db.add(new_dog)
    db.commit()
    db.refresh(new_dog)
    return {"status": "success", "note": new_dog}


@app.get("/dogs")
def get_dogs(db: Session = Depends(get_db)):
    all_dogs = db.query(models.Dog).all()
    return all_dogs


@app.put("/dogs/{dog_id}")
def update_dog(dog_id: UUID, dog: dog, db: Session = Depends(get_db)):
    # Check if the provided dog_id exists in the database
    dog_in_db = db.query(models.Dog).filter(models.Dog.id == dog_id).first()
    if not dog_in_db:
        raise HTTPException(status_code=404, detail="Dog not found")

    # Update the dog's information
    dog_in_db.bark_decibels = dog.bark_decibels

    db.commit()
    db.refresh(dog_in_db)
    return {"status": "success", "note": "Dog updated successfully"}


@app.delete("/dogs/{dog_id}")
def delete_dog(dog_id: UUID, db: Session = Depends(get_db)):
    # Check if the provided dog_id exists in the database
    dog = db.query(models.Dog).filter(models.Dog.id == dog_id).first()
    if not dog:
        raise HTTPException(status_code=404, detail="Dog not found")

    # Delete the dog
    db.delete(dog)
    db.commit()
    return {"status": "success", "note": "Dog deleted successfully"}


# List all dogs in a city
@app.get("/city/{city_name}/dogs")
def get_dogs_in_city(city_name, db: Session = Depends(get_db)):
    city = db.query(models.City).filter(models.City.name == city_name).first()
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")

    dogs = db.query(models.Dog).filter_by(city_id=city.id).all()

    return dogs


@app.post("/city/{city_name}/dogs")
def create_dogs_in_city(city_name, dog: dog, db: Session = Depends(get_db)):
    city = db.query(models.City).filter(models.City.name == city_name).first()
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")

    db_dog = (
        db.query(models.Dog)
        .filter_by(bark_decibels=dog.bark_decibels)
        .first()
    )
    if db_dog:
        db_dog.city_id = city.id
        db.commit()
        db.refresh(db_dog)
        return db_dog
    else:
        new_dog = models.Dog(**dog.dict())
        db.add(new_dog)
        new_dog.city_id = city.id
        db.commit()
        db.refresh(new_dog)
        return new_dog


@app.put("/city/{city_name}/dogs/{dog_id}")
def update_dog_in_city(
    city_name, dog_id: UUID, dog: dog, db: Session = Depends(get_db)
):
    city = db.query(models.City).filter(models.City.name == city_name).first()
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")

    db_dog = db.query(models.Dog).filter_by(id=dog_id, city_id=city.id).first()
    if db_dog is None:
        raise HTTPException(status_code=404, detail="Dog not found in this city")

    db_dog.bark_decibels = dog.bark_decibels
    db_dog.city_id = city.id

    db.commit()
    db.refresh(db_dog)

    return db_dog


@app.delete("/city/{city_name}/dogs/{dog_id}")
def delete_dog_in_city(city_name, dog_id: UUID, db: Session = Depends(get_db)):
    city = db.query(models.City).filter(models.City.name == city_name).first()
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")

    db_dog = db.query(models.Cat).filter_by(id=dog_id, city_id=city.id).first()
    if db_dog is None:
        raise HTTPException(status_code=404, detail="Dog not found in this city")

    db.delete(db_dog)
    db.commit()

    return {"message": "Dog deleted successfully"}


@app.get("/stats/cats/")
def cat_statistics(db: Session = Depends(get_db)):

    query = """
        SELECT 
        cities.id,
        cities.name AS city_name,
        COALESCE(COUNT(cats.id), 0) AS cat_count
        FROM 
            cities
        LEFT JOIN 
            animals ON cities.id = animals.city_id
        LEFT JOIN 
            cats ON animals.id = cats.id
        GROUP BY 
            cities.id, cities.name;

    """
    stats = db.execute(query).fetchall()
    return [
            {"id": row[0], "name": row[1], "total": row[2]}
            for row in stats
        ]


@app.get("/stats/dogs/")
def dog_statistics(db: Session = Depends(get_db)):
    query = text("""
        SELECT DISTINCT ON (cities.name)
        cities.id,
        cities.name AS city_name,
        breed,
        COALESCE(MAX(bark_decibels), 0) AS max_bark_decibels
        FROM
            cities
        LEFT JOIN 
            animals ON cities.id = animals.city_id
        LEFT JOIN 
            dogs ON animals.id = dogs.id
        GROUP BY 
            cities.id, cities.name, breed, bark_decibels;
    """)
    stats = db.execute(query).fetchall()
    
    return  [
        {"id": city_id, "name": name, "animal_breed": breed, "decibels": decibels}
        for city_id, name, breed, decibels in stats
    ]
