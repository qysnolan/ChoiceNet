# import json
#
#
# def JsonUsers(request):
#
#     from accounts.models import User
#
#     user = request.user
#     filtered = evals = Evaluation.objects.user_can_view(request.user)
#
#     columns = ["timeModified", "timeModified", ["teacher__last_name", "teacher__first_name"],
#                "evalType__name", "teacher__departments__name", ["evaluator__last_name", "evaluator__first_name"],
#                "submit", False, False]
#
#     columnSearchable = [False, False, True, True, True, True, False, False, False]