from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from iban_check.iban_validation import check_iban
from iban_check.models import Iban


def main(request):
    previously_checked = Iban.objects.order_by("-created_at")[:5]
    return render(request, "main.html", {"previously_checked": previously_checked})


@require_POST
def validate_iban(request):
    iban: str = request.POST.get("iban_input")
    if not iban:
        return JsonResponse(
            {
                "success": False,
                "msg": "Please input IBAN"
            }
        )
    iban: str = iban.replace(" ", "")  # clean up spaces
    if len(iban) != 22:
        return JsonResponse(
            {
                "success": False,
                "msg": "Please input correct IBAN"
            }
        )

    is_valid: bool = check_iban(iban)
    response: dict = {"success": True, "value": iban, "is_valid": is_valid, "msg": f"{iban} is valid: {is_valid}"}
    Iban.objects.create(
        value=iban,
        is_valid=is_valid
    )
    return JsonResponse(response)
