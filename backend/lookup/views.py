from django.http import JsonResponse
from django.views.decorators.http import require_GET

from .services import lookup_word
from .services import MODEL_NAME


MAX_WORD_LENGTH = 100


@require_GET
def lookup(request):
    word = request.GET.get("word", "").strip()

    if not word:
        return JsonResponse(
            {"error": "Missing required parameter: word"},
            status=400,
        )

    if len(word) > MAX_WORD_LENGTH:
        return JsonResponse(
            {
                "error": f"Word must be {MAX_WORD_LENGTH} characters or fewer."
            },
            status=400,
        )

    result = lookup_word(word)

    return JsonResponse(result)


@require_GET
def health(request):
    return JsonResponse(
        {
            "status": "ok",
            "spacy": True,
            "model": MODEL_NAME,
        }
    )


