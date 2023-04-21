from anakonda.util import jsonify


class TaskController:
    def get_tasks():
        return jsonify(status=501, code=101)

    def get_task(task_id):
        pass

    def create_task():
        pass

    def update_task(task_id):
        pass

    def delete_task(task_id):
        pass
