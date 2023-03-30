import os
import re
import time
from ast import literal_eval

import pywebio
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *

from meili_search import search

pywebio.config(title='问卷星填报挂', theme='minty')


def main():
    put_markdown("""# 问卷星填报挂
    ## 打开问卷地址，F12开启控制台，复制粘贴下面的代码：
    ```javascript
    // 修改userAgent破解微信填写限制
    var customUserAgent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12A365 MicroMessenger/5.4.1 NetType/WIF';
    Object.defineProperty(navigator, 'userAgent', {
      value: customUserAgent,
      writable: false
    });
    
    // 获取问卷题目
    const results = [];
    const fieldsets = document.querySelectorAll('#divQuestion .field-label');
    for (let i = 1; i < fieldsets.length; i++) {
        results.push(fieldsets[i].innerText.replace(/[^\w\u4e00-\u9fa5\u00C0-\u017F（）]/g, ''));
        // 复制到剪贴板
        copy(results);
    }
    console.log(results); 
    ```   

    """)
    img = open('doc.gif', 'rb').read()
    put_image(img, width='100%')
    info = input_group('答案生成：', [
        slider('偏移量（比较专业不要轻易设置，请咨询专业人士）', name="shifting", value=1, step=1, max_value=10,
               min_value=1),
        textarea('执行上面脚本后，在此处CTRL+V', name="questions", rows=20, code={
            'mode': "python",
            'theme': 'darcula'
        })
    ])

    print(f'偏移量:{info["shifting"]}')
    print(f'问题列表:{info["questions"]}')
    shifting = info['shifting']
    questions = literal_eval(info['questions'])
    answer_str = ''
    for index, question in enumerate(questions):
        question = re.sub("\d+", "", question)
        answer = search(question)
        answer_str += f'document.getElementById("q{(index + 1) + shifting}").value = "{answer}"\n';
        print(answer_str)
    put_markdown("# 答案填报");
    img2 = open('doc2.gif', 'rb').read()
    put_image(img2, width='100%')
    put_code(info["questions"], language='python')
    textarea('调整答案删除不必要内容，将下面code粘贴回答题标签页的控制台', value=answer_str, rows=20, code={
        'mode': "python",
        'theme': 'darcula'
    })


if __name__ == '__main__':
    start_server(main, debug=True, port=888)
