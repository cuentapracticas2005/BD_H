import click
from app import create_app, db
from app.models import User, RoleEnum

app = create_app()


@app.cli.command("init-db")
def init_db():
    """Initialize database tables."""
    db.create_all()
    click.echo("Database initialized")


@app.cli.command("create-admin")
@click.option("--username", required=True)
@click.option("--password", required=True)
def create_admin(username: str, password: str):
    """Create initial admin user."""
    if User.query.filter_by(username=username).first():
        click.echo("User already exists")
        return
    user = User(username=username, role=RoleEnum.ADMIN)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    click.echo("Admin user created")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)