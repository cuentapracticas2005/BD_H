import os
from functools import wraps
from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from . import db
from .models import Document

admin_bp = Blueprint("admin", __name__)

ALLOWED_PDF_EXTENSIONS = {"pdf"}


def _allowed_pdf(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_PDF_EXTENSIONS


def admin_required(view_func):
    @wraps(view_func)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash("Permisos insuficientes", "error")
            return redirect(url_for("main.dashboard"))
        return view_func(*args, **kwargs)

    return wrapped


@admin_bp.get("/documents")
@login_required
@admin_required
def documents_list():
    documents = Document.query.order_by(Document.created_at.desc()).all()
    return render_template("admin/documents.html", documents=documents)


@admin_bp.post("/documents")
@login_required
@admin_required
def documents_create():
    form = request.form
    file = request.files.get("pdf")
    if not file or file.filename == "":
        flash("Debe adjuntar un PDF", "error")
        return redirect(url_for("admin.documents_list"))

    if not _allowed_pdf(file.filename):
        flash("Formato inválido. Solo PDF.", "error")
        return redirect(url_for("admin.documents_list"))

    filename = secure_filename(file.filename)
    file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))

    document = Document(
        year=int(form.get("anio")),
        month=form.get("mes"),
        description=form.get("descripcion"),
        plan_number=form.get("numero_plano"),
        size=form.get("tamano"),
        version=form.get("version"),
        drafter=form.get("dibujante"),
        drawn_in=form.get("dibujado_en"),
        pdf_filename=filename,
        created_by_id=current_user.id,
    )
    db.session.add(document)
    db.session.commit()
    flash("Documento creado", "success")
    return redirect(url_for("admin.documents_list"))


@admin_bp.post("/documents/<int:doc_id>/delete")
@login_required
@admin_required
def documents_delete(doc_id: int):
    document = Document.query.get_or_404(doc_id)
    db.session.delete(document)
    db.session.commit()
    flash("Documento eliminado", "success")
    return redirect(url_for("admin.documents_list"))


@admin_bp.post("/documents/<int:doc_id>")
@login_required
@admin_required
def documents_update(doc_id: int):
    document = Document.query.get_or_404(doc_id)
    form = request.form
    document.year = int(form.get("anio"))
    document.month = form.get("mes")
    document.description = form.get("descripcion")
    document.plan_number = form.get("numero_plano")
    document.size = form.get("tamano")
    document.version = form.get("version")
    document.drafter = form.get("dibujante")
    document.drawn_in = form.get("dibujado_en")

    file = request.files.get("pdf")
    if file and file.filename:
        if not _allowed_pdf(file.filename):
            flash("Formato inválido. Solo PDF.", "error")
            return redirect(url_for("admin.documents_list"))
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
        document.pdf_filename = filename

    db.session.commit()
    flash("Documento actualizado", "success")
    return redirect(url_for("admin.documents_list"))