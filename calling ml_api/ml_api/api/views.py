import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def predict_student_performance(request):
    if request.method == 'POST':
        try:
            # Grab input from frontend/POST body
            data = json.loads(request.body)

            # Ensure payload format matches your FastAPI model
            payload = {"hours": data.get("hours")}

            # Call your deployed ML API
            response = requests.post(
                "https://student-performance-predictor-ixru.onrender.com/predict",
                json=payload
            )

            if response.status_code == 200:
                return JsonResponse(response.json(), status=200)
            else:
                return JsonResponse(
                    {"error": "ML API error", "details": response.text},
                    status=response.status_code
                )

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POSTERS allowed"}, status=405)
