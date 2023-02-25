from django.shortcuts import render

from django.http import HttpResponse

def my_view(request):
    if request.method == 'POST':
        # フォームデータを受け取る
        my_data = request.POST.get('my_data')
        # データを処理する
        processed_data = my_data.upper()
        # 結果を返す
        return HttpResponse('Processed data: ' + processed_data)
    else:
        # GETリクエストの場合は、フォームを表示する
        return render(request, 'my_form.html')