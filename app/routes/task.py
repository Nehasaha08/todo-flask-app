from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models import Task

task_bp = Blueprint('task', __name__)

@task_bp.route('/')
def viewtask():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    tasks = Task.query.all()
    return render_template('task.html', tasks=tasks)

@task_bp.route('/add', methods=["POST"])
def addtask():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    title = request.form.get('title')
    if title:
        newtask = Task(title=title, status='pending')
        db.session.add(newtask)
        db.session.commit()
        flash('Task added successfully', 'success')
    return redirect(url_for('task.viewtask'))

@task_bp.route('/toggle/<int:task_id>', methods=["POST"])
def togglestatus(task_id):
    task = db.session.get(Task, task_id)

    if task:
        if task.status == 'pending':
            task.status = 'working'
        elif task.status == 'working':
            task.status = 'done'
        else:
            task.status = 'pending'
        db.session.commit()
    return redirect(url_for('task.viewtask'))

@task_bp.route('/clear', methods=["POST"])
def cleartask():
    Task.query.delete()
    db.session.commit()
    flash('All tasks cleared', 'info')
    return redirect(url_for('task.viewtask'))
