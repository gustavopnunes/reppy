from flask import Blueprint
from app.controllers.user_controller import (create_user,
 delete_user,
 get_user_by_id)


bp = Blueprint("bp_student", __name__, url_prefix='/student')
bp.post("")(create_user)
bp.get("<cpf>")(get_user_by_id)
bp.delete("<cpf>")(delete_user)
bp.patch("")

