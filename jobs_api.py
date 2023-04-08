import logging

from flask import Blueprint, jsonify
from data.jobs import Jobs
from data import db_session

blueprint = Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('job', 'team_leader', 'work_size', 'collaborators', 'is_finished'))
                 for item in jobs]
        })


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_jobs(jobs_id):
    db_sess = db_session.create_session()
    if jobs_id.type != int:
        return jsonify({'error': 'Bad request'})
    job = db_sess.query(Jobs).get(jobs_id)
    if not job:
        return jsonify({'error': 'Not found'})
    return jsonify({'job': job.to_dict(only=('job', 'team_leader', 'work_size', 'collaborators', 'is_finished'))})