from flask import Blueprint, request
from app.models import Item
from app.models import db
from app.forms.item_form import ItemForm


bp = Blueprint('items_route', __name__, url_prefix='/api/items')


@bp.route('/<int:id>', methods=['PUT'])
def update_item():
    form = ItemForm()
    if form.validate_on_submit():
        item_to_edit = Item.query.get(id)
        item_to_edit['happiness'] = form.data['happiness']
        item_to_edit['imageUrl'] = form.data['imageUrl']
        item_to_edit['name'] = form.data['name']
        item_to_edit['price'] = form.data['price']
        item_to_edit['pokemonId'] = form.data['pokemonId']
        db.session.commit()
        return {
              "id": 1,
              "happiness": form.data['happiness'],
              "imageUrl": form.data['imageUrl'],
              "name": form.data['name'],
              "price": form.data['price'],
              "pokemonId": form.data['pokemonId']
        }
    else:
        return {"errors": form.errors}

@bp.route('/<int:id>', methods=['DELETE'])
def delete_item():
    item = Item.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return {"id": id}
