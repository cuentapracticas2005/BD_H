import os
from flask import Blueprint, render_template, redirect, url_for, request, flash, send_from_directory, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from . import db
from .models import Document, RoleEnum

main_bp = Blueprint("main", __name__)

ALLOWED_PDF_EXTENSIONS = {"pdf"}


def allowed_pdf(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_PDF_EXTENSIONS


@main_bp.get("/")
@login_required
def dashboard():
    documents = Document.query.order_by(Document.created_at.desc()).limit(50).all()
    return render_template("dashboard/index.html", documents=documents)


@main_bp.get("/docs/<int:doc_id>/download")
@login_required
def download_doc(doc_id: int):
    document = Document.query.get_or_404(doc_id)
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], document.pdf_filename, as_attachment=True)