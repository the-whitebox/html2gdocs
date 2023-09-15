from docx import Document
from htmldocx import HtmlToDocx

document = Document()
new_parser = HtmlToDocx()
# do stuff to document

html1 = """
<p>No style specified <span width="10" style="color: rgb(235, 107, 86);">[span with color]</span> no style</p>
<p><span style="background-color: rgb(251, 160, 38);">Background color in RGB</span></p>
<p><span style="background-color: #f39e65;">Background color in Hex</span></p>
<p><span style="background-color: orange;">Background color as name</span></p>
<p><span style="color: rgb(161, 145, 231);">Forecolor in RGB</span></p>
<p><span style="color: #9488da;">Forecolor in Hex</span></p>
<p><span style="color: mediumpurple;">Forecolor as name</span></p>
<p><span style="background-color: rgb(71, 85, 119); color: rgb(255, 255, 255);">This sentence has background
        and&nbsp;</span><span style="background-color: rgb(71, 85, 119);"><span style="color: rgb(247, 218, 100);">text
            color</span><span style="color: rgb(100, 100, 100);">&nbsp;</span></span><span
        style="background-color: rgb(71, 85, 119); color: rgb(255, 255, 255);">and<strong> bold </strong><em>italic</em>
        <u>underlined</u> <s>strike</s> styles</span></p>
<p>List</p>
<pre>2 + 3 = 5↵this is code</pre>
<p>A picture from file: <img src='testimg.png' /></p>
<p>A picture from url: <img src='https://raw.githubusercontent.com/pqzx/h2d/master/testimg.png' /></p>
<p>A picture from url that's broken: <img src='https://raw.githubusercontent.com/pqzx/h2d/master/fakeimg.png' /></p>
<h1>heading 1</h1>
<ol>
    <li>Ordered list first item</li>
    <p>Paragraph inserted between items</p>
    <li>Second item</li>
</ol>
<ul style="list-style-type: circle;">
    <li>Unorderd list</li>
    <li>with circle markers</li>
</ul>
<li>List item outside of ul tags</li>
<p>Align left Align leftAlign leftAlign leftAlign leftAlign leftAlign leftAlign leftAlign leftAlign left</p>
<p style="text-align: center;">Align center Align center Align center Align center Align center Align center Align
    center Align center Align center</p>
<p style="text-align: right;">Align Right. Align Right. Align Right. Align Right. Align Right. Align Right. Align Right.
    Align Right.</p>
<p style="text-align: justify;">This sentence is justified. This sentence is justified. This sentence is justified. This
    sentence is justified. This sentence is justified.</p>
<p style="text-align: justify;">Indent 0</p>
<p style="text-align: justify; margin-left: 20px;">Indent 1</p>
<p style="text-align: justify; margin-left: 40px;">Indent 2</p>
<p style="text-align: justify; margin-left: 60px;">Indent 3</p>
<p style="text-align: justify; margin-left: 80px;">Indent 4</p>
<p style="text-align: justify; margin-left: 580px;">Indent max?</p>
<p style="text-align: justify; margin-left: 2.5em;">Indent 2.5em</p>
<p style="text-align: left;">asdfsa</p>
<p style="text-align: left;"><a class="fr-green fr-strong" href="abc://def.ghi" rel="noopener noreferrer"
        target="_blank">link</a></p>
<ol>
    <li>Ordered list</li>
    <ul>
        <li>nested unordered list</li>
        <ul>
            <ol>
        </ul>
</ol>

</ol>
</ul>
"""


html = """

<html>

<head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type">
    <style type="text/css">
        @import url(https://themes.googleusercontent.com/fonts/css?kit=I5iEdlySSZdl8NbVSMZmGRMChRzr_Rz7ANADP5IDsj6Cb-_S5yBlhlqlcdKSB3pi0c_NB-THYsQheuqnlp0ypA);

        .lst-kix_9caylrna3pxw-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_9caylrna3pxw-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_9caylrna3pxw-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_9caylrna3pxw-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_hittx35vxp7o-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_9caylrna3pxw-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_kg1y8wqbxbmm-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_hittx35vxp7o-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_hittx35vxp7o-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_kg1y8wqbxbmm-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_kg1y8wqbxbmm-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_f7hlbl6ncfrb-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_hittx35vxp7o-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_f7hlbl6ncfrb-7>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_rlio3lpkz7jy-1 {
            list-style-type: none
        }

        .lst-kix_hittx35vxp7o-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_f7hlbl6ncfrb-8>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_rlio3lpkz7jy-2 {
            list-style-type: none
        }

        ul.lst-kix_rlio3lpkz7jy-3 {
            list-style-type: none
        }

        .lst-kix_kg1y8wqbxbmm-8>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_rlio3lpkz7jy-4 {
            list-style-type: none
        }

        ul.lst-kix_rlio3lpkz7jy-5 {
            list-style-type: none
        }

        .lst-kix_kg1y8wqbxbmm-7>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_rlio3lpkz7jy-6 {
            list-style-type: none
        }

        .lst-kix_hittx35vxp7o-7>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_rlio3lpkz7jy-7 {
            list-style-type: none
        }

        ul.lst-kix_rlio3lpkz7jy-8 {
            list-style-type: none
        }

        .lst-kix_9caylrna3pxw-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_5ta50c7r3jsb-8>li:before {
            content: "-  "
        }

        .lst-kix_5ta50c7r3jsb-7>li:before {
            content: "-  "
        }

        ul.lst-kix_rlio3lpkz7jy-0 {
            list-style-type: none
        }

        .lst-kix_sq0khldledfw-0>li:before {
            content: "-  "
        }

        .lst-kix_5ta50c7r3jsb-4>li:before {
            content: "-  "
        }

        .lst-kix_5ta50c7r3jsb-6>li:before {
            content: "-  "
        }

        .lst-kix_f7hlbl6ncfrb-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_5ta50c7r3jsb-5>li:before {
            content: "-  "
        }

        .lst-kix_sq0khldledfw-3>li:before {
            content: "-  "
        }

        .lst-kix_f7hlbl6ncfrb-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_sq0khldledfw-2>li:before {
            content: "-  "
        }

        .lst-kix_sq0khldledfw-4>li:before {
            content: "-  "
        }

        .lst-kix_5ta50c7r3jsb-0>li:before {
            content: "-  "
        }

        .lst-kix_5ta50c7r3jsb-2>li:before {
            content: "-  "
        }

        .lst-kix_sq0khldledfw-1>li:before {
            content: "-  "
        }

        .lst-kix_sq0khldledfw-5>li:before {
            content: "-  "
        }

        .lst-kix_f7hlbl6ncfrb-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_hittx35vxp7o-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_f7hlbl6ncfrb-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_5ta50c7r3jsb-3>li:before {
            content: "-  "
        }

        .lst-kix_f7hlbl6ncfrb-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_hittx35vxp7o-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_hittx35vxp7o-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_f7hlbl6ncfrb-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_5ta50c7r3jsb-1>li:before {
            content: "-  "
        }

        ul.lst-kix_5ta50c7r3jsb-2 {
            list-style-type: none
        }

        ul.lst-kix_o1qv3covyuhp-8 {
            list-style-type: none
        }

        ul.lst-kix_5ta50c7r3jsb-3 {
            list-style-type: none
        }

        ul.lst-kix_o1qv3covyuhp-7 {
            list-style-type: none
        }

        ul.lst-kix_5ta50c7r3jsb-4 {
            list-style-type: none
        }

        ul.lst-kix_5ta50c7r3jsb-5 {
            list-style-type: none
        }

        ul.lst-kix_5ta50c7r3jsb-6 {
            list-style-type: none
        }

        ul.lst-kix_sq0khldledfw-3 {
            list-style-type: none
        }

        ul.lst-kix_5ta50c7r3jsb-7 {
            list-style-type: none
        }

        ul.lst-kix_sq0khldledfw-2 {
            list-style-type: none
        }

        .lst-kix_sq0khldledfw-8>li:before {
            content: "-  "
        }

        ul.lst-kix_5ta50c7r3jsb-8 {
            list-style-type: none
        }

        ul.lst-kix_sq0khldledfw-1 {
            list-style-type: none
        }

        ul.lst-kix_sq0khldledfw-0 {
            list-style-type: none
        }

        ul.lst-kix_sq0khldledfw-7 {
            list-style-type: none
        }

        ul.lst-kix_o1qv3covyuhp-0 {
            list-style-type: none
        }

        .lst-kix_sq0khldledfw-6>li:before {
            content: "-  "
        }

        ul.lst-kix_sq0khldledfw-6 {
            list-style-type: none
        }

        .lst-kix_sq0khldledfw-7>li:before {
            content: "-  "
        }

        .lst-kix_rlio3lpkz7jy-8>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_sq0khldledfw-5 {
            list-style-type: none
        }

        ul.lst-kix_o1qv3covyuhp-2 {
            list-style-type: none
        }

        ul.lst-kix_sq0khldledfw-4 {
            list-style-type: none
        }

        ul.lst-kix_o1qv3covyuhp-1 {
            list-style-type: none
        }

        .lst-kix_twa7fmlm0myo-8>li:before {
            content: "-  "
        }

        ul.lst-kix_o1qv3covyuhp-4 {
            list-style-type: none
        }

        ul.lst-kix_o1qv3covyuhp-3 {
            list-style-type: none
        }

        ul.lst-kix_5ta50c7r3jsb-0 {
            list-style-type: none
        }

        ul.lst-kix_o1qv3covyuhp-6 {
            list-style-type: none
        }

        ul.lst-kix_5ta50c7r3jsb-1 {
            list-style-type: none
        }

        ul.lst-kix_sq0khldledfw-8 {
            list-style-type: none
        }

        ul.lst-kix_o1qv3covyuhp-5 {
            list-style-type: none
        }

        .lst-kix_rlio3lpkz7jy-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_rlio3lpkz7jy-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_rlio3lpkz7jy-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_m2o39wug3stw-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_rlio3lpkz7jy-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_rlio3lpkz7jy-6>li:before {
            content: "\0025cf   "
        }

        ul.lst-kix_hrj1mobvgozk-0 {
            list-style-type: none
        }

        .lst-kix_rlio3lpkz7jy-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_m2o39wug3stw-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_m2o39wug3stw-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_m2o39wug3stw-8>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_7wh80aky3tl-7 {
            list-style-type: none
        }

        ul.lst-kix_7wh80aky3tl-8 {
            list-style-type: none
        }

        .lst-kix_hmzln0wvfp6b-2>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_7wh80aky3tl-5 {
            list-style-type: none
        }

        ul.lst-kix_7wh80aky3tl-6 {
            list-style-type: none
        }

        ul.lst-kix_7wh80aky3tl-3 {
            list-style-type: none
        }

        .lst-kix_m2o39wug3stw-3>li:before {
            content: "\0025cf   "
        }

        ul.lst-kix_7wh80aky3tl-4 {
            list-style-type: none
        }

        .lst-kix_hmzln0wvfp6b-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_hmzln0wvfp6b-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_rlio3lpkz7jy-0>li:before {
            content: "\0025cf   "
        }

        ul.lst-kix_7wh80aky3tl-1 {
            list-style-type: none
        }

        .lst-kix_m2o39wug3stw-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_kg1y8wqbxbmm-2>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_7wh80aky3tl-2 {
            list-style-type: none
        }

        .lst-kix_rlio3lpkz7jy-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_m2o39wug3stw-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_kg1y8wqbxbmm-3>li:before {
            content: "\0025cf   "
        }

        ul.lst-kix_7wh80aky3tl-0 {
            list-style-type: none
        }

        .lst-kix_hmzln0wvfp6b-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_hmzln0wvfp6b-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_hmzln0wvfp6b-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_9caylrna3pxw-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_hmzln0wvfp6b-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_9caylrna3pxw-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_kg1y8wqbxbmm-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_m2o39wug3stw-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_kg1y8wqbxbmm-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_m2o39wug3stw-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_9caylrna3pxw-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_7wh80aky3tl-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_yhup4qprrvne-1>li:before {
            content: "-  "
        }

        .lst-kix_7wh80aky3tl-2>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_z1v77ckegazw-8 {
            list-style-type: none
        }

        ul.lst-kix_z1v77ckegazw-7 {
            list-style-type: none
        }

        ul.lst-kix_z1v77ckegazw-6 {
            list-style-type: none
        }

        ul.lst-kix_z1v77ckegazw-5 {
            list-style-type: none
        }

        ul.lst-kix_z1v77ckegazw-4 {
            list-style-type: none
        }

        .lst-kix_7wh80aky3tl-8>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_z1v77ckegazw-3 {
            list-style-type: none
        }

        ul.lst-kix_z1v77ckegazw-2 {
            list-style-type: none
        }

        ul.lst-kix_z1v77ckegazw-1 {
            list-style-type: none
        }

        ul.lst-kix_z1v77ckegazw-0 {
            list-style-type: none
        }

        .lst-kix_7wh80aky3tl-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_hmzln0wvfp6b-1>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_m37p1hpp2vp0-7 {
            list-style-type: none
        }

        ul.lst-kix_m37p1hpp2vp0-8 {
            list-style-type: none
        }

        .lst-kix_z1v77ckegazw-2>li:before {
            content: "-  "
        }

        .lst-kix_z1v77ckegazw-4>li:before {
            content: "-  "
        }

        .lst-kix_h80lx66szhhi-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_yhup4qprrvne-7>li:before {
            content: "-  "
        }

        .lst-kix_h80lx66szhhi-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_twa7fmlm0myo-1>li:before {
            content: "-  "
        }

        .lst-kix_yhup4qprrvne-3>li:before {
            content: "-  "
        }

        .lst-kix_yhup4qprrvne-5>li:before {
            content: "-  "
        }

        .lst-kix_twa7fmlm0myo-7>li:before {
            content: "-  "
        }

        .lst-kix_twa7fmlm0myo-3>li:before {
            content: "-  "
        }

        .lst-kix_7wh80aky3tl-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_z1v77ckegazw-6>li:before {
            content: "-  "
        }

        .lst-kix_z1v77ckegazw-8>li:before {
            content: "-  "
        }

        .lst-kix_twa7fmlm0myo-5>li:before {
            content: "-  "
        }

        .lst-kix_h80lx66szhhi-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_x01xw83wyg8l-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_x01xw83wyg8l-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_iwj9ow65dqjp-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_iwj9ow65dqjp-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_o1qv3covyuhp-1>li:before {
            content: "-  "
        }

        .lst-kix_x01xw83wyg8l-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_h80lx66szhhi-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_iwj9ow65dqjp-8>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_m37p1hpp2vp0-0 {
            list-style-type: none
        }

        ul.lst-kix_m37p1hpp2vp0-1 {
            list-style-type: none
        }

        ul.lst-kix_m37p1hpp2vp0-2 {
            list-style-type: none
        }

        .lst-kix_z1v77ckegazw-0>li:before {
            content: "-  "
        }

        ul.lst-kix_m37p1hpp2vp0-3 {
            list-style-type: none
        }

        ul.lst-kix_m37p1hpp2vp0-4 {
            list-style-type: none
        }

        ul.lst-kix_m37p1hpp2vp0-5 {
            list-style-type: none
        }

        .lst-kix_h80lx66szhhi-0>li:before {
            content: "\0025cf   "
        }

        ul.lst-kix_m37p1hpp2vp0-6 {
            list-style-type: none
        }

        .lst-kix_iwj9ow65dqjp-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_o1qv3covyuhp-7>li:before {
            content: "-  "
        }

        .lst-kix_hrj1mobvgozk-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_o1qv3covyuhp-3>li:before {
            content: "-  "
        }

        .lst-kix_iwj9ow65dqjp-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_o1qv3covyuhp-5>li:before {
            content: "-  "
        }

        .lst-kix_x01xw83wyg8l-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_m37p1hpp2vp0-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_jbk0ytbwq90f-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_jbk0ytbwq90f-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_hrj1mobvgozk-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_m37p1hpp2vp0-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_m37p1hpp2vp0-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_m37p1hpp2vp0-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_m37p1hpp2vp0-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_jbk0ytbwq90f-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_jbk0ytbwq90f-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_hrj1mobvgozk-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_m37p1hpp2vp0-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_m37p1hpp2vp0-8>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_kg1y8wqbxbmm-4 {
            list-style-type: none
        }

        ul.lst-kix_kg1y8wqbxbmm-3 {
            list-style-type: none
        }

        ul.lst-kix_kg1y8wqbxbmm-6 {
            list-style-type: none
        }

        .lst-kix_jbk0ytbwq90f-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_jbk0ytbwq90f-7>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_kg1y8wqbxbmm-5 {
            list-style-type: none
        }

        ul.lst-kix_kg1y8wqbxbmm-8 {
            list-style-type: none
        }

        ul.lst-kix_kg1y8wqbxbmm-7 {
            list-style-type: none
        }

        .lst-kix_m37p1hpp2vp0-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_jbk0ytbwq90f-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_jbk0ytbwq90f-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_hrj1mobvgozk-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_hbs1lkdqencn-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_hbs1lkdqencn-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_hrj1mobvgozk-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_hbs1lkdqencn-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_hrj1mobvgozk-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_hrj1mobvgozk-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_hrj1mobvgozk-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_m37p1hpp2vp0-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_hrj1mobvgozk-4>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_iwj9ow65dqjp-4 {
            list-style-type: none
        }

        ul.lst-kix_iwj9ow65dqjp-5 {
            list-style-type: none
        }

        ul.lst-kix_iwj9ow65dqjp-2 {
            list-style-type: none
        }

        ul.lst-kix_iwj9ow65dqjp-3 {
            list-style-type: none
        }

        ul.lst-kix_m2o39wug3stw-5 {
            list-style-type: none
        }

        ul.lst-kix_iwj9ow65dqjp-8 {
            list-style-type: none
        }

        ul.lst-kix_h80lx66szhhi-0 {
            list-style-type: none
        }

        ul.lst-kix_m2o39wug3stw-6 {
            list-style-type: none
        }

        ul.lst-kix_h80lx66szhhi-1 {
            list-style-type: none
        }

        ul.lst-kix_m2o39wug3stw-7 {
            list-style-type: none
        }

        ul.lst-kix_iwj9ow65dqjp-6 {
            list-style-type: none
        }

        ul.lst-kix_h80lx66szhhi-2 {
            list-style-type: none
        }

        ul.lst-kix_m2o39wug3stw-8 {
            list-style-type: none
        }

        ul.lst-kix_iwj9ow65dqjp-7 {
            list-style-type: none
        }

        ul.lst-kix_h80lx66szhhi-3 {
            list-style-type: none
        }

        ul.lst-kix_h80lx66szhhi-4 {
            list-style-type: none
        }

        ul.lst-kix_h80lx66szhhi-5 {
            list-style-type: none
        }

        ul.lst-kix_h80lx66szhhi-6 {
            list-style-type: none
        }

        ul.lst-kix_h80lx66szhhi-7 {
            list-style-type: none
        }

        ul.lst-kix_iwj9ow65dqjp-0 {
            list-style-type: none
        }

        ul.lst-kix_h80lx66szhhi-8 {
            list-style-type: none
        }

        ul.lst-kix_iwj9ow65dqjp-1 {
            list-style-type: none
        }

        .lst-kix_jbk0ytbwq90f-4>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_m2o39wug3stw-1 {
            list-style-type: none
        }

        ul.lst-kix_m2o39wug3stw-2 {
            list-style-type: none
        }

        ul.lst-kix_m2o39wug3stw-3 {
            list-style-type: none
        }

        ul.lst-kix_m2o39wug3stw-4 {
            list-style-type: none
        }

        ul.lst-kix_m2o39wug3stw-0 {
            list-style-type: none
        }

        .lst-kix_hbs1lkdqencn-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_hbs1lkdqencn-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_hbs1lkdqencn-6>li:before {
            content: "\0025cf   "
        }

        ul.lst-kix_9caylrna3pxw-0 {
            list-style-type: none
        }

        ul.lst-kix_9caylrna3pxw-1 {
            list-style-type: none
        }

        .lst-kix_hbs1lkdqencn-4>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_9caylrna3pxw-4 {
            list-style-type: none
        }

        ul.lst-kix_9caylrna3pxw-5 {
            list-style-type: none
        }

        .lst-kix_hbs1lkdqencn-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_hbs1lkdqencn-5>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_9caylrna3pxw-2 {
            list-style-type: none
        }

        ul.lst-kix_9caylrna3pxw-3 {
            list-style-type: none
        }

        ul.lst-kix_9caylrna3pxw-8 {
            list-style-type: none
        }

        ul.lst-kix_9caylrna3pxw-6 {
            list-style-type: none
        }

        ul.lst-kix_9caylrna3pxw-7 {
            list-style-type: none
        }

        ul.lst-kix_kg1y8wqbxbmm-0 {
            list-style-type: none
        }

        ul.lst-kix_kg1y8wqbxbmm-2 {
            list-style-type: none
        }

        ul.lst-kix_kg1y8wqbxbmm-1 {
            list-style-type: none
        }

        ul.lst-kix_hbs1lkdqencn-1 {
            list-style-type: none
        }

        ul.lst-kix_hittx35vxp7o-3 {
            list-style-type: none
        }

        ul.lst-kix_hbs1lkdqencn-2 {
            list-style-type: none
        }

        ul.lst-kix_hittx35vxp7o-2 {
            list-style-type: none
        }

        ul.lst-kix_hbs1lkdqencn-3 {
            list-style-type: none
        }

        ul.lst-kix_hittx35vxp7o-1 {
            list-style-type: none
        }

        ul.lst-kix_hbs1lkdqencn-4 {
            list-style-type: none
        }

        ul.lst-kix_hittx35vxp7o-0 {
            list-style-type: none
        }

        ul.lst-kix_hbs1lkdqencn-5 {
            list-style-type: none
        }

        ul.lst-kix_hbs1lkdqencn-6 {
            list-style-type: none
        }

        ul.lst-kix_hbs1lkdqencn-7 {
            list-style-type: none
        }

        .lst-kix_7wh80aky3tl-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_7wh80aky3tl-5>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_f7hlbl6ncfrb-8 {
            list-style-type: none
        }

        ul.lst-kix_hbs1lkdqencn-8 {
            list-style-type: none
        }

        ul.lst-kix_f7hlbl6ncfrb-7 {
            list-style-type: none
        }

        .lst-kix_7wh80aky3tl-3>li:before {
            content: "\0025cf   "
        }

        ul.lst-kix_hbs1lkdqencn-0 {
            list-style-type: none
        }

        .lst-kix_yhup4qprrvne-0>li:before {
            content: "-  "
        }

        ul.lst-kix_f7hlbl6ncfrb-6 {
            list-style-type: none
        }

        ul.lst-kix_f7hlbl6ncfrb-5 {
            list-style-type: none
        }

        ul.lst-kix_f7hlbl6ncfrb-4 {
            list-style-type: none
        }

        ul.lst-kix_hittx35vxp7o-8 {
            list-style-type: none
        }

        ul.lst-kix_f7hlbl6ncfrb-3 {
            list-style-type: none
        }

        ul.lst-kix_hittx35vxp7o-7 {
            list-style-type: none
        }

        ul.lst-kix_f7hlbl6ncfrb-2 {
            list-style-type: none
        }

        ul.lst-kix_hittx35vxp7o-6 {
            list-style-type: none
        }

        ul.lst-kix_f7hlbl6ncfrb-1 {
            list-style-type: none
        }

        .lst-kix_7wh80aky3tl-7>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_hittx35vxp7o-5 {
            list-style-type: none
        }

        ul.lst-kix_f7hlbl6ncfrb-0 {
            list-style-type: none
        }

        ul.lst-kix_hittx35vxp7o-4 {
            list-style-type: none
        }

        .lst-kix_h80lx66szhhi-7>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_hrj1mobvgozk-5 {
            list-style-type: none
        }

        ul.lst-kix_hrj1mobvgozk-6 {
            list-style-type: none
        }

        .lst-kix_hmzln0wvfp6b-0>li:before {
            content: "\0025cf   "
        }

        ul.lst-kix_hrj1mobvgozk-7 {
            list-style-type: none
        }

        .lst-kix_twa7fmlm0myo-0>li:before {
            content: "-  "
        }

        ul.lst-kix_hrj1mobvgozk-8 {
            list-style-type: none
        }

        ul.lst-kix_hrj1mobvgozk-1 {
            list-style-type: none
        }

        ul.lst-kix_hrj1mobvgozk-2 {
            list-style-type: none
        }

        ul.lst-kix_hrj1mobvgozk-3 {
            list-style-type: none
        }

        ul.lst-kix_hrj1mobvgozk-4 {
            list-style-type: none
        }

        .lst-kix_z1v77ckegazw-1>li:before {
            content: "-  "
        }

        .lst-kix_z1v77ckegazw-5>li:before {
            content: "-  "
        }

        .lst-kix_h80lx66szhhi-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_twa7fmlm0myo-2>li:before {
            content: "-  "
        }

        .lst-kix_h80lx66szhhi-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_yhup4qprrvne-8>li:before {
            content: "-  "
        }

        .lst-kix_z1v77ckegazw-3>li:before {
            content: "-  "
        }

        .lst-kix_twa7fmlm0myo-6>li:before {
            content: "-  "
        }

        ul.lst-kix_x01xw83wyg8l-5 {
            list-style-type: none
        }

        ul.lst-kix_x01xw83wyg8l-6 {
            list-style-type: none
        }

        ul.lst-kix_x01xw83wyg8l-3 {
            list-style-type: none
        }

        ul.lst-kix_x01xw83wyg8l-4 {
            list-style-type: none
        }

        ul.lst-kix_x01xw83wyg8l-7 {
            list-style-type: none
        }

        .lst-kix_yhup4qprrvne-2>li:before {
            content: "-  "
        }

        .lst-kix_yhup4qprrvne-6>li:before {
            content: "-  "
        }

        ul.lst-kix_x01xw83wyg8l-8 {
            list-style-type: none
        }

        .lst-kix_twa7fmlm0myo-4>li:before {
            content: "-  "
        }

        ul.lst-kix_x01xw83wyg8l-1 {
            list-style-type: none
        }

        ul.lst-kix_x01xw83wyg8l-2 {
            list-style-type: none
        }

        .lst-kix_yhup4qprrvne-4>li:before {
            content: "-  "
        }

        ul.lst-kix_x01xw83wyg8l-0 {
            list-style-type: none
        }

        .lst-kix_z1v77ckegazw-7>li:before {
            content: "-  "
        }

        .lst-kix_x01xw83wyg8l-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_x01xw83wyg8l-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_iwj9ow65dqjp-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_iwj9ow65dqjp-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_o1qv3covyuhp-0>li:before {
            content: "-  "
        }

        .lst-kix_iwj9ow65dqjp-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_x01xw83wyg8l-2>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_jbk0ytbwq90f-8 {
            list-style-type: none
        }

        ul.lst-kix_jbk0ytbwq90f-7 {
            list-style-type: none
        }

        ul.lst-kix_jbk0ytbwq90f-6 {
            list-style-type: none
        }

        ul.lst-kix_twa7fmlm0myo-4 {
            list-style-type: none
        }

        ul.lst-kix_jbk0ytbwq90f-5 {
            list-style-type: none
        }

        ul.lst-kix_twa7fmlm0myo-3 {
            list-style-type: none
        }

        ul.lst-kix_jbk0ytbwq90f-4 {
            list-style-type: none
        }

        ul.lst-kix_twa7fmlm0myo-2 {
            list-style-type: none
        }

        ul.lst-kix_jbk0ytbwq90f-3 {
            list-style-type: none
        }

        ul.lst-kix_twa7fmlm0myo-1 {
            list-style-type: none
        }

        ul.lst-kix_jbk0ytbwq90f-2 {
            list-style-type: none
        }

        ul.lst-kix_twa7fmlm0myo-0 {
            list-style-type: none
        }

        ul.lst-kix_jbk0ytbwq90f-1 {
            list-style-type: none
        }

        ul.lst-kix_jbk0ytbwq90f-0 {
            list-style-type: none
        }

        .lst-kix_x01xw83wyg8l-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_iwj9ow65dqjp-7>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_twa7fmlm0myo-8 {
            list-style-type: none
        }

        .lst-kix_h80lx66szhhi-1>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_twa7fmlm0myo-7 {
            list-style-type: none
        }

        ul.lst-kix_twa7fmlm0myo-6 {
            list-style-type: none
        }

        ul.lst-kix_twa7fmlm0myo-5 {
            list-style-type: none
        }

        ul.lst-kix_hmzln0wvfp6b-0 {
            list-style-type: none
        }

        ul.lst-kix_hmzln0wvfp6b-2 {
            list-style-type: none
        }

        ul.lst-kix_hmzln0wvfp6b-1 {
            list-style-type: none
        }

        .lst-kix_o1qv3covyuhp-8>li:before {
            content: "-  "
        }

        li.li-bullet-0:before {
            margin-left: -18pt;
            white-space: nowrap;
            display: inline-block;
            min-width: 18pt
        }

        ul.lst-kix_yhup4qprrvne-0 {
            list-style-type: none
        }

        .lst-kix_o1qv3covyuhp-4>li:before {
            content: "-  "
        }

        ul.lst-kix_yhup4qprrvne-3 {
            list-style-type: none
        }

        ul.lst-kix_yhup4qprrvne-4 {
            list-style-type: none
        }

        .lst-kix_o1qv3covyuhp-2>li:before {
            content: "-  "
        }

        .lst-kix_o1qv3covyuhp-6>li:before {
            content: "-  "
        }

        ul.lst-kix_yhup4qprrvne-1 {
            list-style-type: none
        }

        ul.lst-kix_yhup4qprrvne-2 {
            list-style-type: none
        }

        ul.lst-kix_yhup4qprrvne-7 {
            list-style-type: none
        }

        ul.lst-kix_hmzln0wvfp6b-4 {
            list-style-type: none
        }

        ul.lst-kix_yhup4qprrvne-8 {
            list-style-type: none
        }

        ul.lst-kix_hmzln0wvfp6b-3 {
            list-style-type: none
        }

        ul.lst-kix_yhup4qprrvne-5 {
            list-style-type: none
        }

        ul.lst-kix_hmzln0wvfp6b-6 {
            list-style-type: none
        }

        ul.lst-kix_yhup4qprrvne-6 {
            list-style-type: none
        }

        .lst-kix_x01xw83wyg8l-8>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_hmzln0wvfp6b-5 {
            list-style-type: none
        }

        ul.lst-kix_hmzln0wvfp6b-8 {
            list-style-type: none
        }

        ul.lst-kix_hmzln0wvfp6b-7 {
            list-style-type: none
        }

        ol {
            margin: 0;
            padding: 0
        }

        table td,
        table th {
            padding: 0
        }

        .c11 {
            border-right-style: solid;
            padding: 5pt 5pt 5pt 5pt;
            border-bottom-color: #000000;
            border-top-width: 1pt;
            border-right-width: 1pt;
            border-left-color: #000000;
            vertical-align: top;
            border-right-color: #000000;
            border-left-width: 1pt;
            border-top-style: solid;
            background-color: #032140;
            border-left-style: solid;
            border-bottom-width: 1pt;
            width: 129pt;
            border-top-color: #000000;
            border-bottom-style: solid
        }

        .c25 {
            border-right-style: solid;
            padding: 5pt 5pt 5pt 5pt;
            border-bottom-color: #000000;
            border-top-width: 1pt;
            border-right-width: 1pt;
            border-left-color: #000000;
            vertical-align: top;
            border-right-color: #000000;
            border-left-width: 1pt;
            border-top-style: solid;
            border-left-style: solid;
            border-bottom-width: 1pt;
            width: 167.1pt;
            border-top-color: #000000;
            border-bottom-style: solid
        }

        .c20 {
            border-right-style: solid;
            padding: 5pt 5pt 5pt 5pt;
            border-bottom-color: #000000;
            border-top-width: 1pt;
            border-right-width: 1pt;
            border-left-color: #000000;
            vertical-align: top;
            border-right-color: #000000;
            border-left-width: 1pt;
            border-top-style: solid;
            border-left-style: solid;
            border-bottom-width: 1pt;
            width: 344.2pt;
            border-top-color: #000000;
            border-bottom-style: solid
        }

        .c10 {
            margin-left: 36pt;
            padding-top: 0pt;
            padding-left: 0pt;
            padding-bottom: 16pt;
            line-height: 1.15;
            orphans: 2;
            widows: 2;
            text-align: justify
        }

        .c6 {
            margin-left: 72pt;
            padding-top: 0pt;
            padding-left: 0pt;
            padding-bottom: 16pt;
            line-height: 1.15;
            orphans: 2;
            widows: 2;
            text-align: justify
        }

        .c47 {
            color: #002140;
            font-weight: 600;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 13pt;
            font-family: "Source Serif Pro";
            font-style: normal
        }

        .c3 {
            color: #000000;
            font-weight: 400;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 11pt;
            font-family: "Raleway";
            font-style: normal
        }

        .c0 {
            padding-top: 16pt;
            padding-bottom: 16pt;
            line-height: 1.15;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        .c39 {
            color: #002140;
            font-weight: 600;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 20pt;
            font-family: "Source Serif Pro";
            font-style: normal
        }

        .c13 {
            color: #333333;
            font-weight: 400;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 11pt;
            font-family: "Raleway";
            font-style: normal
        }

        .c29 {
            color: #1292d3;
            font-weight: 400;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 11pt;
            font-family: "Raleway";
            font-style: normal
        }

        .c9 {
            color: #002140;
            font-weight: 600;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 14pt;
            font-family: "Source Serif Pro";
            font-style: normal
        }

        .c5 {
            color: #000000;
            font-weight: 400;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 11pt;
            font-family: "Raleway";
            font-style: italic
        }

        .c4 {
            color: #1292d3;
            font-weight: 400;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 11pt;
            font-family: "Raleway";
            font-style: italic
        }

        .c1 {
            padding-top: 0pt;
            padding-bottom: 16pt;
            line-height: 1.15;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        .c16 {
            padding-top: 0pt;
            padding-bottom: 0pt;
            line-height: 1.0;
            orphans: 2;
            widows: 2;
            text-align: left;
            height: 11pt
        }

        .c31 {
            color: #1292d3;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 11pt;
            font-family: "Raleway";
            font-style: normal
        }

        .c38 {
            color: #1292d3;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 1pt;
            font-family: "Roboto";
            font-style: normal
        }

        .c37 {
            color: #434343;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 11pt;
            font-family: "Raleway";
            font-style: normal
        }

        .c26 {
            padding-top: 0pt;
            padding-bottom: 0pt;
            line-height: 1.0;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        .c8 {
            padding-top: 0pt;
            padding-bottom: 16pt;
            line-height: 1.15;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        .c36 {
            color: #333333;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 11pt;
            font-family: "Roboto";
            font-style: normal
        }

        .c45 {
            color: #333333;
            font-weight: 400;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 11pt;
            font-family: "Raleway"
        }

        .c27 {
            padding-top: 0pt;
            padding-bottom: 0pt;
            line-height: 1.15;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        .c33 {
            color: #1291d2;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 10pt;
            font-family: "Raleway";
            font-style: normal
        }

        .c54 {
            color: #000000;
            font-weight: 400;
            font-size: 11pt;
            font-family: "Arial";
            font-style: normal
        }

        .c55 {
            color: #333333;
            font-weight: 400;
            font-size: 12pt;
            font-family: "Roboto";
            font-style: normal
        }

        .c7 {
            text-decoration-skip-ink: none;
            -webkit-text-decoration-skip: none;
            color: #1292d3;
            font-weight: 700;
            text-decoration: underline
        }

        .c28 {
            padding-top: 0pt;
            padding-bottom: 0pt;
            line-height: 1.0;
            text-align: left
        }

        .c61 {
            vertical-align: baseline;
            font-size: 11pt;
            font-family: "Raleway";
            font-style: normal
        }

        .c53 {
            padding-top: 0pt;
            padding-bottom: 0pt;
            line-height: 1.15;
            text-align: center
        }

        .c46 {
            padding-top: 0pt;
            padding-bottom: 16pt;
            line-height: 1.15;
            text-align: left
        }

        .c21 {
            text-decoration-skip-ink: none;
            -webkit-text-decoration-skip: none;
            color: #1155cc;
            text-decoration: underline
        }

        .c15 {
            padding-top: 0pt;
            padding-bottom: 16pt;
            line-height: 1.15;
            text-align: justify
        }

        .c64 {
            color: #002140;
            font-weight: 500;
            font-size: 11pt;
            font-family: "Raleway"
        }

        .c60 {
            font-weight: 400;
            font-size: 11pt;
            font-family: "Raleway";
            font-style: normal
        }

        .c22 {
            border-spacing: 0;
            border-collapse: collapse;
            margin-right: auto
        }

        .c50 {
            color: #434343;
            font-size: 14pt;
            font-family: "Source Serif Pro";
            font-style: normal
        }

        .c40 {
            padding-top: 0pt;
            padding-bottom: 16pt;
            line-height: 1.15;
            text-align: right
        }

        .c48 {
            font-size: 14pt;
            font-family: "Source Serif Pro";
            color: #002140;
            font-weight: 600
        }

        .c17 {
            orphans: 2;
            widows: 2;
            height: 11pt
        }

        .c51 {
            font-weight: 600;
            font-size: 14pt;
            font-family: "Source Serif Pro"
        }

        .c52 {
            font-weight: 400;
            font-size: 12pt;
            font-family: "Raleway"
        }

        .c65 {
            color: #434343;
            font-size: 11pt;
            font-family: "Raleway"
        }

        .c24 {
            padding: 0;
            margin: 0
        }

        .c35 {
            margin-left: 36pt;
            height: 14pt
        }

        .c34 {
            orphans: 2;
            widows: 2
        }

        .c12 {
            color: #1292d3;
            font-style: italic
        }

        .c43 {
            margin-left: 36pt;
            padding-left: 0pt
        }

        .c23 {
            margin-left: 72pt;
            padding-left: 0pt
        }

        .c59 {
            max-width: 451.4pt;
            padding: 72pt 72pt 72pt 72pt
        }

        .c2 {
            color: inherit;
            text-decoration: inherit
        }

        .c41 {
            border: 1px solid black;
            margin: 5px
        }

        .c49 {
            text-decoration: none;
            vertical-align: baseline
        }

        .c44 {
            background-color: #ffffff
        }

        .c14 {
            height: 0pt
        }

        .c32 {
            height: 11pt
        }

        .c62 {
            text-decoration: none
        }

        .c63 {
            font-weight: 400
        }

        .c42 {
            height: 20pt
        }

        .c56 {
            height: 14pt
        }

        .c58 {
            font-size: 12pt
        }

        .c57 {
            color: #000000
        }

        .c19 {
            color: #f3f3f3
        }

        .c30 {
            font-weight: 700
        }

        .c18 {
            font-style: italic
        }

        .title {
            padding-top: 0pt;
            color: #002140;
            font-weight: 600;
            font-size: 24pt;
            padding-bottom: 0pt;
            font-family: "Source Serif Pro";
            line-height: 1.0;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        .subtitle {
            padding-top: 0pt;
            color: #666666;
            font-size: 15pt;
            padding-bottom: 16pt;
            font-family: "Arial";
            line-height: 1.15;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        li {
            color: #333333;
            font-size: 11pt;
            font-family: "Raleway"
        }

        p {
            margin: 0;
            color: #333333;
            font-size: 11pt;
            font-family: "Raleway"
        }

        h1 {
            padding-top: 16pt;
            color: #002140;
            font-weight: 600;
            font-size: 20pt;
            padding-bottom: 16pt;
            font-family: "Source Serif Pro";
            line-height: 1.15;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        h2 {
            padding-top: 16pt;
            color: #002140;
            font-weight: 600;
            font-size: 16pt;
            padding-bottom: 16pt;
            font-family: "Source Serif Pro";
            line-height: 1.15;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        h3 {
            padding-top: 0pt;
            color: #002140;
            font-weight: 600;
            font-size: 14pt;
            padding-bottom: 16pt;
            font-family: "Source Serif Pro";
            line-height: 1.15;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        h4 {
            padding-top: 0pt;
            color: #333333;
            font-weight: 700;
            font-size: 12pt;
            padding-bottom: 16pt;
            font-family: "Roboto";
            line-height: 1.15;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        h5 {
            padding-top: 12pt;
            color: #666666;
            font-size: 11pt;
            padding-bottom: 4pt;
            font-family: "Raleway";
            line-height: 1.15;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        h6 {
            padding-top: 12pt;
            color: #666666;
            font-size: 11pt;
            padding-bottom: 4pt;
            font-family: "Raleway";
            line-height: 1.15;
            page-break-after: avoid;
            font-style: italic;
            orphans: 2;
            widows: 2;
            text-align: left
        }
    </style>
</head>

<body class="c44 c59 doc-content">
    <div>
        <p class="c8 c32"><span class="c38 c30"></span></p>
        <p class="c8 c32"><span class="c30 c38"></span></p>
    </div>
    <hr>
    <p class="c8 c32"><span class="c36 c63"></span></p>
    <p class="c15 c34"><span class="c13">When producing content, each component of a page can contribute in its own way
            towards the SEO performance of the page, and therefore it is important to ensure each element is considered
            carefully to help the content rank more effectively for the targeted keywords.</span></p>
    <p class="c15 c34"><span class="c13">This document is intended to act as a template to be used when creating new
            content. It contains two key sections: </span></p>
    <ul class="c24 lst-kix_iwj9ow65dqjp-0 start">
        <li class="c10 li-bullet-0"><span class="c13">A content template that can be filled out when developing a new
                piece of content, with SEO considerations for each section.</span></li>
        <li class="c10 li-bullet-0"><span>A section which provides detailed explanations, best practices and key
                considerations for each element of the template further down in the document (</span><span
                class="c12">seen in this font</span><span class="c3">).</span></li>
    </ul>
    <h1 class="c0" id="h.ylyalq8x3s4e"><span class="c39">SEO Content Template</span></h1>
    <h3 class="c1" id="h.kmzoeh39sfn6"><span>Content Purpose and meta information (for content writers)</span></h3>
    <p class="c27 c32"><span class="c37 c30"></span></p><a id="t.a87ade598cc7d2fd27b4aa2a7ba538087b2bd4ec"></a><a
        id="t.0"></a>
    <table class="c22">
        <tr class="c14">
            <td class="c11" colspan="1" rowspan="1">
                <p class="c28"><span class="c19 c30">Scope </span><span class="c7"><a class="c2"
                            href="#h.okim5323btee">(?)</a></span></p>
            </td>
            <td class="c20" colspan="1" rowspan="1">
                <p class="c28"><span class="c5">What do we want to achieve from the content?</span></p>
                <p class="c28 c32"><span class="c3"></span></p>
            </td>
        </tr>
        <tr class="c14">
            <td class="c11" colspan="1" rowspan="1">
                <p class="c28"><span class="c19 c30">Primary keywords </span><span class="c7"><a class="c2"
                            href="#h.etltxujwp0f0">(?)</a></span><span class="c19 c30">&nbsp; </span></p>
            </td>
            <td class="c20" colspan="1" rowspan="1">
                <p class="c27"><span class="c5">What are the main keywords we are targeting with this content?</span>
                </p>
                <p class="c27 c32"><span class="c5"></span></p><a id="t.c2ab6cb3994b667c9584baa154118e32508a8920"></a><a
                    id="t.1"></a>
                <table class="c22">
                    <tr class="c14">
                        <td class="c25" colspan="1" rowspan="1">
                            <p class="c28"><span class="c3">Keyword</span></p>
                        </td>
                        <td class="c25" colspan="1" rowspan="1">
                            <p class="c28"><span class="c3">Monthly Search Volume</span></p>
                        </td>
                    </tr>
                    <tr class="c14">
                        <td class="c25" colspan="1" rowspan="1">
                            <p class="c28 c32"><span class="c3"></span></p>
                        </td>
                        <td class="c25" colspan="1" rowspan="1">
                            <p class="c28 c32"><span class="c3"></span></p>
                        </td>
                    </tr>
                    <tr class="c14">
                        <td class="c25" colspan="1" rowspan="1">
                            <p class="c28 c32"><span class="c3"></span></p>
                        </td>
                        <td class="c25" colspan="1" rowspan="1">
                            <p class="c28 c32"><span class="c3"></span></p>
                        </td>
                    </tr>
                    <tr class="c14">
                        <td class="c25" colspan="1" rowspan="1">
                            <p class="c28 c32"><span class="c3"></span></p>
                        </td>
                        <td class="c25" colspan="1" rowspan="1">
                            <p class="c28 c32"><span class="c3"></span></p>
                        </td>
                    </tr>
                </table>
                <p class="c27 c32"><span class="c3"></span></p>
                <p class="c27 c32"><span class="c3"></span></p>
            </td>
        </tr>
        <tr class="c14">
            <td class="c11" colspan="1" rowspan="1">
                <p class="c28"><span class="c19 c30">Secondary keywords </span><span class="c7"><a class="c2"
                            href="#h.etltxujwp0f0">(?) </a></span></p>
            </td>
            <td class="c20" colspan="1" rowspan="1">
                <p class="c27"><span class="c5">What are the keywords which we are targeting, but may not be the primary
                        focus of the content?</span></p>
                <p class="c27 c32"><span class="c3"></span></p><a id="t.c2ab6cb3994b667c9584baa154118e32508a8920"></a><a
                    id="t.2"></a>
                <table class="c22">
                    <tr class="c14">
                        <td class="c25" colspan="1" rowspan="1">
                            <p class="c28"><span class="c3">Keyword</span></p>
                        </td>
                        <td class="c25" colspan="1" rowspan="1">
                            <p class="c28"><span class="c3">Monthly Search Volume</span></p>
                        </td>
                    </tr>
                    <tr class="c14">
                        <td class="c25" colspan="1" rowspan="1">
                            <p class="c28 c32"><span class="c3"></span></p>
                        </td>
                        <td class="c25" colspan="1" rowspan="1">
                            <p class="c28 c32"><span class="c3"></span></p>
                        </td>
                    </tr>
                    <tr class="c14">
                        <td class="c25" colspan="1" rowspan="1">
                            <p class="c28 c32"><span class="c3"></span></p>
                        </td>
                        <td class="c25" colspan="1" rowspan="1">
                            <p class="c28 c32"><span class="c3"></span></p>
                        </td>
                    </tr>
                    <tr class="c14">
                        <td class="c25" colspan="1" rowspan="1">
                            <p class="c28 c32"><span class="c3"></span></p>
                        </td>
                        <td class="c25" colspan="1" rowspan="1">
                            <p class="c28 c32"><span class="c3"></span></p>
                        </td>
                    </tr>
                </table>
                <p class="c27 c32"><span class="c3"></span></p>
                <p class="c27 c32"><span class="c3"></span></p>
            </td>
        </tr>
        <tr class="c14">
            <td class="c11" colspan="1" rowspan="1">
                <p class="c28"><span class="c19 c30">Meta Title </span><span class="c7"><a class="c2"
                            href="#h.io5wxfvr2pno">(?)</a></span></p>
            </td>
            <td class="c20" colspan="1" rowspan="1">
                <p class="c27"><span class="c5">What is the title of this content?</span></p>
                <p class="c27 c32"><span class="c3"></span></p>
            </td>
        </tr>
        <tr class="c14">
            <td class="c11" colspan="1" rowspan="1">
                <p class="c28"><span class="c19 c30">Meta Description </span><span class="c7"><a class="c2"
                            href="#h.io5wxfvr2pno">(?)</a></span></p>
            </td>
            <td class="c20" colspan="1" rowspan="1">
                <p class="c8"><span class="c18">General outline/introduction to the content of the page</span></p>
            </td>
        </tr>
        <tr class="c14">
            <td class="c11" colspan="1" rowspan="1">
                <p class="c28"><span class="c19 c30">Benchmark content </span><span class="c7"><a class="c2"
                            href="#h.ruuka4lir6uz">(?)</a></span></p>
            </td>
            <td class="c20" colspan="1" rowspan="1">
                <p class="c27"><span class="c5">URLs of benchmark content</span></p>
                <p class="c27 c32"><span class="c5"></span></p>
                <p class="c8"><span class="c5">&lt;Example URL&gt;</span></p>
                <p class="c8"><span class="c5">&lt;Example URL&gt;</span></p>
            </td>
        </tr>
        <tr class="c14">
            <td class="c11" colspan="1" rowspan="1">
                <p class="c28"><span class="c19 c30">Word count </span><span class="c7"><a class="c2"
                            href="#h.ecsrlmjf8amh">(?)</a></span></p>
            </td>
            <td class="c20" colspan="1" rowspan="1">
                <p class="c27"><span class="c5">Target word count range</span></p>
            </td>
        </tr>
    </table>
    <p class="c27 c32"><span class="c3"></span></p>
    <h3 class="c1 c56" id="h.67v2fhy2rfik"><span class="c9"></span></h3>
    <hr style="page-break-before:always;display:none;">
    <h3 class="c1 c56" id="h.jcoi54yngno2"><span class="c9"></span></h3>
    <h3 class="c1" id="h.kmpfasen2gm0"><span>On page structure (for content writers)</span></h3><a
        id="t.a636fefcf8cd8b6060471e05437cb52cf9aaee8b"></a><a id="t.3"></a>
    <table class="c22">
        <tr class="c14">
            <td class="c11" colspan="1" rowspan="1">
                <p class="c28"><span class="c19 c30">H1 Tag </span><span class="c7"><a class="c2"
                            href="#h.laztkd6ihn2e">(?)</a></span></p>
            </td>
            <td class="c20" colspan="1" rowspan="1">
                <p class="c27"><span class="c5">The main heading on the page</span></p>
            </td>
        </tr>
        <tr class="c14">
            <td class="c11" colspan="1" rowspan="1">
                <p class="c28"><span class="c19 c30">Opening content </span><span class="c7"><a class="c2"
                            href="#h.9lpv2s4oakdg">(?)</a></span></p>
            </td>
            <td class="c20" colspan="1" rowspan="1">
                <p class="c27"><span class="c5">The first section of content that is on the page below the H1</span></p>
            </td>
        </tr>
        <tr class="c14">
            <td class="c11" colspan="1" rowspan="1">
                <p class="c28"><span class="c19 c30">Above the fold content considerations </span><span class="c7"><a
                            class="c2" href="#h.t5i98p2r0rn">(?)</a></span></p>
            </td>
            <td class="c20" colspan="1" rowspan="1">
                <p class="c27"><span class="c5">Considerations for content that should appear above the fold</span></p>
            </td>
        </tr>
        <tr class="c14">
            <td class="c11" colspan="1" rowspan="1">
                <p class="c28"><span class="c19 c30">H2 Tags </span><span class="c7"><a class="c2"
                            href="#h.rxboup2i3y6c">(?)</a></span></p>
            </td>
            <td class="c20" colspan="1" rowspan="1">
                <p class="c27"><span class="c5">Section subheadings</span></p>
            </td>
        </tr>
        <tr class="c14">
            <td class="c11" colspan="1" rowspan="1">
                <p class="c28"><span class="c19 c30">H3 Tags - </span><span class="c19">where applicable </span><span
                        class="c7"><a class="c2" href="#h.rxboup2i3y6c">(?)</a></span></p>
            </td>
            <td class="c20" colspan="1" rowspan="1">
                <p class="c27"><span class="c18 c57">Section subheadings</span></p>
            </td>
        </tr>
        <tr class="c14">
            <td class="c11" colspan="1" rowspan="1">
                <p class="c28"><span class="c19 c30">H4 Tags - </span><span class="c19">where applicable </span><span
                        class="c7"><a class="c2" href="#h.rxboup2i3y6c">(?)</a></span></p>
            </td>
            <td class="c20" colspan="1" rowspan="1">
                <p class="c27"><span class="c57 c18">Section subheadings</span></p>
            </td>
        </tr>
        <tr class="c14">
            <td class="c11" colspan="1" rowspan="1">
                <p class="c28"><span class="c19 c30">H5 Tags - </span><span class="c19">where applicable </span><span
                        class="c7"><a class="c2" href="#h.rxboup2i3y6c">(?)</a></span></p>
            </td>
            <td class="c20" colspan="1" rowspan="1">
                <p class="c27"><span class="c57 c18">Section subheadings</span></p>
            </td>
        </tr>
        <tr class="c14">
            <td class="c11" colspan="1" rowspan="1">
                <p class="c28"><span class="c19 c30">H6 Tags - </span><span class="c19">where applicable </span><span
                        class="c7"><a class="c2" href="#h.rxboup2i3y6c">(?)</a></span></p>
            </td>
            <td class="c20" colspan="1" rowspan="1">
                <p class="c27"><span class="c57 c18">Section subheadings</span></p>
            </td>
        </tr>
    </table>
    <p class="c15 c17"><span class="c13"></span></p>
    <h3 class="c1" id="h.xk661zizozjb"><span class="c9">SEO Considerations </span></h3>
    <p class="c27 c32"><span class="c30 c37"></span></p><a id="t.47f9063a63bfdb2f93572c310dcfecb760f5068c"></a><a
        id="t.4"></a>
    <table class="c22">
        <thead>
            <tr class="c14">
                <td class="c11" colspan="1" rowspan="1">
                    <p class="c28"><span class="c19 c30">URL </span><span class="c7"><a class="c2"
                                href="#h.nawhvqj590d6">(?)</a></span></p>
                </td>
                <td class="c20" colspan="1" rowspan="1">
                    <p class="c8"><span class="c18">www.domain.com/example-content</span></p>
                </td>
        <tbody></tbody>
        </tr>
        <tr class="c14">
            <td class="c11" colspan="1" rowspan="1">
                <p class="c28"><span class="c19 c30">Breadcrumbs </span><span class="c7"><a class="c2"
                            href="#h.tpa67q7tly31">(?)</a></span></p>
            </td>
            <td class="c20" colspan="1" rowspan="1">
                <p class="c8"><span class="c18">Site &gt; Topic &gt; Article</span></p>
            </td>
        </tr>
        <tr class="c14">
            <td class="c11" colspan="1" rowspan="1">
                <p class="c28"><span class="c19 c30">Parent or Child page </span><span class="c7"><a class="c2"
                            href="#h.es5gng2bgbyy">(?)</a></span></p>
            </td>
            <td class="c20" colspan="1" rowspan="1">
                <p class="c27"><span class="c49 c63 c18 c65">Where does this content fit within the content
                        hierarchy?</span></p>
            </td>
        </tr>
        <tr class="c14">
            <td class="c11" colspan="1" rowspan="1">
                <p class="c28"><span class="c19 c30">Internal linking opportunities </span><span class="c7"><a
                            class="c2" href="#h.jpf0doe0a8cm">(?)</a></span></p>
            </td>
            <td class="c20" colspan="1" rowspan="1">
                <p class="c27 c32"><span class="c3"></span></p><a id="t.dc2d46375c0ad210075b505cc367b40755e326e0"></a><a
                    id="t.5"></a>
                <table class="c22">
                    <tr class="c14">
                        <td class="c25" colspan="1" rowspan="1">
                            <p class="c26"><span class="c3">Page to link to</span></p>
                        </td>
                        <td class="c25" colspan="1" rowspan="1">
                            <p class="c26"><span class="c3">Suggested anchor text</span></p>
                        </td>
                    </tr>
                    <tr class="c14">
                        <td class="c25" colspan="1" rowspan="1">
                            <p class="c16"><span class="c3"></span></p>
                        </td>
                        <td class="c25" colspan="1" rowspan="1">
                            <p class="c16"><span class="c3"></span></p>
                        </td>
                    </tr>
                    <tr class="c14">
                        <td class="c25" colspan="1" rowspan="1">
                            <p class="c16"><span class="c3"></span></p>
                        </td>
                        <td class="c25" colspan="1" rowspan="1">
                            <p class="c16"><span class="c3"></span></p>
                        </td>
                    </tr>
                </table>
                <p class="c27 c32"><span class="c3"></span></p>
            </td>
        </tr>
        <tr class="c14">
            <td class="c11" colspan="1" rowspan="1">
                <p class="c28"><span class="c19 c30">Featured snippet opportunities </span><span class="c7"><a
                            class="c2" href="#h.ef496j5q1ah2">(?)</a></span></p>
            </td>
            <td class="c20" colspan="1" rowspan="1">
                <p class="c27"><span class="c5">Please show screenshots of any featured snippets we are targeting</span>
                </p>
            </td>
        </tr>
        </thead>
    </table>
    <p class="c15 c17"><span class="c13"></span></p>
    <h3 class="c1" id="h.kjzez1ajn2bc"><span class="c9">Other considerations</span></h3>
    <p class="c27 c32"><span class="c37 c30"></span></p><a id="t.9289fa33abbf346c8d82b2de9b5debd4d23fc89c"></a><a
        id="t.6"></a>
    <table class="c22">
        <tr class="c14">
            <td class="c11" colspan="1" rowspan="1">
                <p class="c28"><span class="c19 c30">Word count </span></p>
            </td>
            <td class="c20" colspan="1" rowspan="1">
                <p class="c27"><span class="c5">1000 words</span></p>
            </td>
        </tr>
        <tr class="c14">
            <td class="c11" colspan="1" rowspan="1">
                <p class="c28"><span class="c19 c30">Benchmark content </span></p>
            </td>
            <td class="c20" colspan="1" rowspan="1">
                <p class="c46"><span class="c3">Sample URL/s</span></p>
            </td>
        </tr>
        <tr class="c14">
            <td class="c11" colspan="1" rowspan="1">
                <p class="c28"><span class="c61 c19 c30 c62">Additional info</span></p>
            </td>
            <td class="c20" colspan="1" rowspan="1">
                <p class="c46"><span class="c3">Please see below: </span></p>
                <p class="c46"><span class="c3">https://domain.com/frequently-asked-questions </span></p>
                <p class="c46"><span class="c3">https://domain.com/termsandconditions </span></p>
                <p class="c46"><span class="c3">https://domain.com/blog/salary-sacrifice-employers-protection </span>
                </p>
            </td>
        </tr>
    </table>
    <p class="c46 c32"><span class="c13"></span></p>
    <h1 class="c0 c42" id="h.ibqejuaprzpz"><span class="c39"></span></h1>
    <p class="c8 c32"><span class="c13"></span></p>
    <p class="c8 c32"><span class="c13"></span></p>
    <p class="c8 c32"><span class="c13"></span></p>
    <p class="c8 c32"><span class="c13"></span></p>
    <p class="c8 c32"><span class="c13"></span></p>
    <p class="c8 c32"><span class="c13"></span></p>
    <p class="c8 c32"><span class="c13"></span></p>
    <h1 class="c0" id="h.ah91dodyy20g"><span class="c39">Content Ideation</span></h1>
    <h3 class="c1" id="h.okim5323btee"><span>Scope</span></h3>
    <p class="c15 c34"><span class="c4">The scope of the page should be the first consideration when creating new
            content. We want to make sure that the content fulfils a purpose, and is differentiated from the content
            existing on the site already.</span></p>
    <p class="c15 c34"><span class="c4">There are several methods we can use to create content ideas and understand its
            scope:</span></p>
    <ul class="c24 lst-kix_h80lx66szhhi-0 start">
        <li class="c10 li-bullet-0"><span class="c4">Keyword gap analysis - our keyword gap analysis highlights relevant
                keywords that we do not rank for that our competitors rank within the top 20 searches for. This shows
                where there are opportunities to target these keywords on our site with new content.</span></li>
        <li class="c10 li-bullet-0"><span class="c12">Keyword universe analysis - </span><span class="c12">our keyword
                universe</span><sup><a href="#cmnt1" id="cmnt_ref1">[a]</a></sup><span class="c4">&nbsp;utilises
                extensive keyword research, incorporating the keyword gap analysis, to produce a vast list of relevant
                keywords that could be used as content ideas. We may want to look for keywords that have high volume but
                are more competitive, or more niche, long tail keywords with fewer monthly searches, but are less
                competitive and more likely to convert to a click.</span></li>
        <li class="c10 li-bullet-0"><span class="c4">Competitor analysis - monitoring our competitors to see if there
                are any pieces of content that are performing well for them, or if there are content areas that we are
                missing on our site that we could do better. This differs from keyword gap analysis, which focuses on
                specific keywords, whereas holistic competitor analysis can identify entire content themes or sections
                of a site that aren&rsquo;t present on our site.</span></li>
        <li class="c10 li-bullet-0"><span class="c4">Monitoring industry news/events - this is effective for identifying
                a recent hot topic or trend in the industry that we feel we could comment on and create content
                around.</span></li>
        <li class="c10 li-bullet-0"><span class="c4">Internal campaigns and business developments - any new developments
                from the business that we want to shout about should be a source of content that no other competitors
                have.</span></li>
    </ul>
    <h3 class="c1" id="h.etltxujwp0f0"><span class="c9">Primary and Secondary Keywords</span></h3>
    <p class="c15 c34"><span class="c4">Identifying the primary and secondary keywords that we want to target with our
            content is a crucial step, and should be carried out alongside identifying the scope and purpose of the
            content. This can be done through utilising keyword research, such as our keyword universe and keyword gap
            analysis.</span></p>
    <p class="c15 c34"><span class="c4">Primary keywords should be the core focus of the content, whereas the secondary
            keywords should be relevant to the primary keywords, but support the content rather than being the primary
            focus.</span></p>
    <p class="c15 c34"><span class="c12">We want to make sure that we won&rsquo;t be competing with our own pages which
            are already targeting certain keywords. This is what is known as keyword cannibalisation. To check for this,
            search in Google for: &lsquo;site:sungardas.com &ldquo;KEYWORD HERE&rdquo;, which will bring up a list of
            all the pages on the site which currently rank for the specified keyword. </span></p>
    <h3 class="c1" id="h.bqnxm8j7yzeu"><span class="c9">E-A-T considerations</span></h3>
    <p class="c8"><span class="c4">E-A-T stands for expertise, authority and trustworthiness, and they are a set of
            parameters which have been important for SEO since the August 2018 &ldquo;medic update&rdquo; from Google.
            They act as measures of a page&rsquo;s quality, which can have an impact on how well a page ranks. E-A-T is
            even more important for certain topics, especially when there are significant consequences for the
            information being shared. As a lot of the content on our site relates to business security and recovery,
            e-a-t is something that we should take seriously as we will likely be judged on these factors more than many
            other industries.</span></p>
    <p class="c8"><span class="c4">Here are some guidelines to consider for each elements of E-A-T when creating new
            content, as well as more generally across the site:</span></p>
    <ul class="c24 lst-kix_9caylrna3pxw-0 start">
        <li class="c8 c43 li-bullet-0"><span class="c4">Expertise</span></li>
    </ul>
    <ul class="c24 lst-kix_9caylrna3pxw-1 start">
        <li class="c8 c23 li-bullet-0"><span class="c4">We need to understand what it is that the user is searching for.
                Identify what is currently ranking in the top 3 positions for our keywords, and understand the
                content/information that is being provided.</span></li>
        <li class="c8 c23 li-bullet-0"><span class="c4">Once we understand the user intent, we can think about how we
                can tailor our content to meet the users intent, and convey our understanding of the topic.</span></li>
        <li class="c8 c23 li-bullet-0"><span class="c4">We also want to make sure that our copy is concise yet
                comprehensive, we don&rsquo;t want to give generic answers which won&rsquo;t distinguish our content,
                and nor do we want to write content that is too in depth and won&rsquo;t engage readers. There is a
                delicate balance to convey expertise in a concise way.</span></li>
        <li class="c8 c23 li-bullet-0"><span class="c4">We can also try and understand the next query that a searcher is
                likely to make after the initial query. This will allow us to add the responses to those questions to
                our page as well. Again, anticipating and understanding user intent is key in demonstrating
                expertise.</span></li>
    </ul>
    <ul class="c24 lst-kix_9caylrna3pxw-0">
        <li class="c8 c43 li-bullet-0"><span class="c4">Authority</span></li>
    </ul>
    <ul class="c24 lst-kix_9caylrna3pxw-1 start">
        <li class="c8 c23 li-bullet-0"><span class="c4">Search engines evaluate how authoritative content is based on
                several factors, including the author, the content itself, and the site that the page sits on. </span>
        </li>
        <li class="c8 c23 li-bullet-0"><span class="c4">If the new content is closely related to all the other content
                on your site, and the author has been proven to have authority in the field, then it is more likely to
                be seen as more authoritative by search engines.</span></li>
        <li class="c8 c23 li-bullet-0"><span class="c4">Generating backlinks from others in the industry is another way
                to demonstrate the authority of your site.</span></li>
        <li class="c8 c23 li-bullet-0"><span class="c4">Working on brand recognition through social media shares,
                article mentions and branded search performance will help indicate to search engines that we are an
                authority in our own right.</span></li>
    </ul>
    <ul class="c24 lst-kix_9caylrna3pxw-0">
        <li class="c8 c43 li-bullet-0"><span class="c4">Trustworthiness</span></li>
    </ul>
    <ul class="c24 lst-kix_9caylrna3pxw-1 start">
        <li class="c8 c23 li-bullet-0"><span class="c4">This point is all about consistency and customer experience.
                Trust is generated through consistently providing users with a great experience, resulting in positive
                reviews and recognition.</span></li>
        <li class="c8 c23 li-bullet-0"><span class="c4">Displaying user reviews/feedback on the site can help improve
                trustworthiness.</span></li>
        <li class="c8 c23 li-bullet-0"><span class="c4">It is also important to be open, honest and accessible when
                trying to improve trustworthiness. Having contact information clearly displayed on the page &nbsp;for
                the author, or website owners is a good example of this.</span></li>
        <li class="c8 c23 li-bullet-0"><span class="c4">Using HTTPS rather than HTTP domains aids
                trustworthiness.</span></li>
        <li class="c8 c23 li-bullet-0"><span class="c12">Having privacy policies and T&amp;C&rsquo;s clearly linked to
                on the footer of the site is also important.</span></li>
    </ul>
    <h1 class="c0" id="h.io5wxfvr2pno"><span>Meta Information</span></h1>
    <p class="c8"><span class="c48">Meta title</span></p>
    <p class="c15 c34"><span class="c12">The title tag of a page is an important factor for the ranking of a page. The
            title is what appears as the blue text on the </span><span class="c12">search engine results page
            (SERP)</span><span class="c12">&nbsp;so should be easily readable, and clearly outline the scope/purpose of
            the content of your page. An example of a SERP can be seen </span><span class="c21 c18"><a class="c2"
                href="https://www.google.com/url?q=https://www.google.com/search?q%3Dsungard%2Bavailability%2Bservices%26oq%3Dsungard%2Ba%26aqs%3Dchrome.0.0j69i57j0l2j46i175i199j69i61l2j69i60.2829j0j7%26sourceid%3Dchrome%26ie%3DUTF-8&amp;sa=D&amp;source=editors&amp;ust=1692706675965981&amp;usg=AOvVaw0pXFO9vwkxGmjSH1J-UY3D">here</a></span><span
            class="c4">. </span></p>
    <ul class="c24 lst-kix_f7hlbl6ncfrb-0 start">
        <li class="c10 li-bullet-0"><span class="c4">The title of the page should be 50-60 characters long, in order to
                avoid being truncated (cut off and replaced by an ellipses).</span></li>
        <li class="c10 li-bullet-0"><span class="c12">The title of a page should contain your primary keyword, and
                potentially a secondary keyword. We want to avoid </span><span class="c21 c18"><a class="c2"
                    href="https://www.google.com/url?q=https://developers.google.com/search/docs/advanced/guidelines/irrelevant-keywords&amp;sa=D&amp;source=editors&amp;ust=1692706675966882&amp;usg=AOvVaw10p8rtDmWJKCuPNlNlmPxZ">keyword
                    stuffing</a></span><span class="c4">&nbsp;in the title, and want to make sure that the title reads
                well, so only include keywords where they would naturally appear.</span></li>
        <li class="c10 li-bullet-0"><span class="c12">The title tag should be different from any other title used on
                your site. To check this quickly, </span><span class="c12">&lsquo;site:sungardas.com &ldquo;YOUR MAIN
                KEYWORD HERE&rdquo; &lsquo; in Google to see what other content exists around your article
                subject.</span></li>
    </ul>
    <p class="c8"><span class="c48">Meta description</span></p>
    <p class="c15 c34"><span class="c12">Although not a direct ranking factor, the meta description should still be
            optimised as it can have a significant impact on the click through rate of the page from the SERP. The
            description </span><span class="c12 c44">should be used to provide a brief description of the page, and
            should go hand in hand with the meta title to give the user a clear understanding of the purpose of the page
            and what they will find if they click on the link.</span></p>
    <p class="c15 c34"><span class="c4">Here are some key considerations when writing the meta description:</span></p>
    <ul class="c24 lst-kix_m2o39wug3stw-0 start">
        <li class="c10 li-bullet-0"><span class="c12">Maximum of 160 characters to avoid being truncated - you can use a
                tool </span><span class="c21 c18"><a class="c2"
                    href="https://www.google.com/url?q=https://www.seomofo.com/snippet-optimizer.html&amp;sa=D&amp;source=editors&amp;ust=1692706675968179&amp;usg=AOvVaw2HEp9w6YaZf-7aIfqlvVgH">like
                    this</a></span><span class="c4">&nbsp;to test the appearance of your description and title in the
                SERP.</span></li>
        <li class="c10 li-bullet-0"><span class="c4">Make sure that your primary keyword is included in the description.
                Any other targeted keywords included in the description should occur naturally.</span></li>
        <li class="c10 li-bullet-0"><span class="c12">Avoid keyword stuffing, keywords in the description have
            </span><span class="c21 c18"><a class="c2"
                    href="https://www.google.com/url?q=https://developers.google.com/search/blog/2009/09/google-does-not-use-keywords-meta-tag&amp;sa=D&amp;source=editors&amp;ust=1692706675968847&amp;usg=AOvVaw1Adi6o9DNF61zIzlYI75Xl">no
                    impact on page ranking</a></span><span class="c4">&nbsp;for keywords.</span></li>
        <li class="c10 li-bullet-0"><span class="c12">Including a call to action in the description is often an
                effective way of improving the click through rate of a page </span><span class="c12">(eg. look, read,
                offers, more info, discover more)</span><span class="c4">.</span></li>
    </ul>
    <h3 class="c1" id="h.nawhvqj590d6"><span>URL </span></h3>
    <p class="c15 c34"><span class="c4">Although not a direct ranking factor, the URL or a page should still be
            optimised as it can affect the click through rate of the page from the SERP. </span></p>
    <ul class="c24 lst-kix_jbk0ytbwq90f-0 start">
        <li class="c10 li-bullet-0"><span class="c4">Having a short URL that is reflective of the content on the page is
                important.</span></li>
        <li class="c10 li-bullet-0"><span class="c4">Generally, the URL should be reflective of the meta title.</span>
        </li>
        <li class="c10 li-bullet-0"><span class="c4">You can remove connecting words such as &ldquo;and&rdquo; from the
                URL to keep it more concise.</span></li>
        <li class="c10 li-bullet-0"><span class="c4">Can help the user understand the topic of the page</span></li>
    </ul>
    <h3 class="c1" id="h.tpa67q7tly31"><span>Breadcrumbs</span></h3>
    <p class="c15 c34"><span class="c4">Breadcrumbs are a small text path which indicates where in the site the user
            currently is. There should be a logical trail of where the content sits on your site, and how a user might
            navigate there from your home page.</span></p>
    <p class="c15 c34"><span class="c12">Where possible, breadcrumbs should be used to help both users and search
            engines to navigate and understand the structure of the </span><span class="c12">site</span><span
            class="c4">. This can bolster the page&rsquo;s visibility as search engines can better understand the page
            and how it relates to the rest of your site.</span></p>
    <p class="c15 c34"><span class="c4">Additionally, search engines can display breadcrumbs on the SERP, which can give
            users an idea of your site structure and content before clicking onto your site, which can help to improve
            the click through rate.</span></p>
    <p class="c15 c34"><span class="c4">&nbsp; </span></p>
    <h1 class="c0" id="h.wtmtvar3cq2u"><span>Content Structure</span></h1>
    <h3 class="c1" id="h.laztkd6ihn2e"><span>H1 Heading </span></h3>
    <p class="c15 c34"><span class="c4">This title should match the meta title of the page, minus any branding, to
            ensure consistency. Generally, only one H1 should be used on one page.</span></p>
    <h3 class="c1" id="h.9lpv2s4oakdg"><span class="c9">Opening content &nbsp;</span></h3>
    <p class="c15 c34"><span class="c4">The first paragraph of copy on the page is very important in SEO terms. As the
            first segment of copy that the user and search engines will see on the page, this segment should act as a
            succinct, information rich summary of what&rsquo;s on the page.</span></p>
    <p class="c15 c34"><span class="c4">The primary keyword of the page should feature within this paragraph, ideally
            within the first 10 words if possible. The other primary and secondary keywords should also feature in this
            first content block where they naturally fit, but don&rsquo;t stuff the keywords in there if it makes the
            content unreadable.</span></p>
    <h3 class="c1" id="h.t5i98p2r0rn"><span class="c9">Above the fold content </span></h3>
    <p class="c8"><span class="c4">Content that appears above the fold (everything that is visible to the user without
            scrolling down) should be targeted towards engaging the user, and should be a good reflection of the content
            that is on the page. A large proportion of this above the fold content will likely be taken up with your
            site navigation, but the H1 title, first paragraph and potentially an image, should all be optimised using
            the guidelines above to make them as engaging as possible and keep the user on the page.</span></p>
    <p class="c15 c34"><span class="c4">A user should be able to look at the above the fold content and be able to
            understand the purpose of the page, and be engaged/intrigued enough to want to scroll further down the page.
            Content below the fold should provide further detail and context for the summary above the fold. </span></p>
    <h3 class="c1" id="h.rxboup2i3y6c"><span>H2, H3, H4, H5, H6 Headings </span></h3>
    <p class="c15 c34"><span class="c12">The subsections of your content should be easily identifiable using subheading.
            T</span><span class="c12">his is crucial for SEO</span><span class="c4">, as this not only helps users and
            search engines understand the structure of the page more easily, but well optimised subheadings can also
            lead to being displayed as featured snippets for some searches.</span></p>
    <p class="c15 c34"><span class="c4">You don&rsquo;t need to use each heading number in every piece of content that
            you create. Typically you would just use H2 headings as subheadings of the H1 on the page. H3&rsquo;s are
            then used as sub-headings of the H2&rsquo;s on your page, and so on. Unless the new content is incredibly in
            depth, it&rsquo;s unlikely that you will need to use H6 headings, but they are available if need be.</span>
    </p>
    <p class="c15 c17"><span class="c4"></span></p>
    <p class="c15 c17"><span class="c4"></span></p>
    <p class="c15 c17"><span class="c4"></span></p>
    <p class="c15 c34"><span class="c4">An example structure of a page might be:</span></p>
    <p class="c15 c34"><span class="c4">H1 - Page Title</span></p>
    <ul class="c24 lst-kix_rlio3lpkz7jy-0 start">
        <li class="c10 li-bullet-0"><span class="c4">H2 subheading</span></li>
    </ul>
    <ul class="c24 lst-kix_rlio3lpkz7jy-1 start">
        <li class="c6 li-bullet-0"><span class="c4">H3 subheading</span></li>
        <li class="c6 li-bullet-0"><span class="c4">H3 subheading</span></li>
    </ul>
    <ul class="c24 lst-kix_rlio3lpkz7jy-0">
        <li class="c10 li-bullet-0"><span class="c4">H2 Subheading</span></li>
        <li class="c10 li-bullet-0"><span class="c4">H2 subheading</span></li>
    </ul>
    <ul class="c24 lst-kix_rlio3lpkz7jy-1 start">
        <li class="c6 li-bullet-0"><span class="c4">H3 subheading</span></li>
    </ul>
    <p class="c15 c34"><span class="c4">General guidelines for optimising subheadings:</span></p>
    <ul class="c24 lst-kix_x01xw83wyg8l-0 start">
        <li class="c10 li-bullet-0"><span class="c4">Use keywords where possible, but as always, the headings should be
                readable and not keyword stuffed</span></li>
        <li class="c10 li-bullet-0"><span class="c4">Under each subheading, the first few sentences should summarise the
                subsection</span></li>
        <li class="c10 li-bullet-0"><span class="c12">A FAQ section on the page works very well for targeting featured
                snippets and appearing as an answer to the &ldquo;frequently asked&rdquo; section of Google. The
                questions should be posed using a heading tag, and the answer should be written in full within the
                subsequent sentences.</span></li>
    </ul>
    <h3 class="c1" id="h.jpf0doe0a8cm"><span>Internal linking opportunities </span></h3>
    <p class="c15 c34"><span class="c12">While writing the copy for the new content, we should be mindful of the
            existing content on our site that we can link to from the new page. Where it makes sense to, we should be
            linking to these other pages from our new content, and vice versa where possible. It is best to link to
            other content on the site that is related to the content you are linking from, as this helps search engines
            and users understand the context of the content and its relevance to other content on the site. </span><span
            class="c12">For example, if we had a new case study that we wanted on the site, and it covered DRaaS, we
            would want to link through to the </span><span class="c21 c18"><a class="c2"
                href="https://www.google.com/url?q=https://www.sungardas.com/en-us/services/connected-recovery/disaster-recovery-as-a-service-draas/&amp;sa=D&amp;source=editors&amp;ust=1692706675975596&amp;usg=AOvVaw3IvOUJ3JQ8CxnrDRN6l7Bk">DRaaS
                page</a></span><span class="c12">, any relevant </span><span class="c18 c21"><a class="c2"
                href="https://www.google.com/url?q=https://www.sungardas.com/en-us/blog/what-is-disaster-recovery-as-a-service-draas/&amp;sa=D&amp;source=editors&amp;ust=1692706675976197&amp;usg=AOvVaw32B5DctZJAKhJvuHJ0mmh2">blog
                posts</a></span><span class="c12">, and potentially the </span><span class="c21 c18"><a class="c2"
                href="https://www.google.com/url?q=https://www.sungardas.com/en-us/partners/technology-partners/dell-technologies/&amp;sa=D&amp;source=editors&amp;ust=1692706675976581&amp;usg=AOvVaw3wogZmKwZ7H_u9Jc51EQ8N">partner
                pages</a></span><span class="c12">&nbsp;who helped to provide the solution.</span><sup><a href="#cmnt2"
                id="cmnt_ref2">[b]</a></sup></p>
    <p class="c15 c34"><span class="c4">Internal linking helps search engines understand and crawl your site better, and
            can understand that pages on your site with the most internal links are likely to be the most important
            pages to crawl and index.</span></p>
    <p class="c15 c34"><span class="c4">To get a better understanding of the content that we may want to link to, or
            have a link to the new page, we can use the site:brand &ldquo;keyword&rdquo; search on Google to find
            related content on our site to link. Alternatively, you could use the site search function that is on the
            site already.</span></p>
    <p class="c15 c17"><span class="c4"></span></p>
    <p class="c15 c17"><span class="c4"></span></p>
    <p class="c15 c34"><span class="c12">There are also further considerations for internal linking:</span></p>
    <ul class="c24 lst-kix_7wh80aky3tl-0 start">
        <li class="c1 c43 li-bullet-0">
            <h3 id="h.9pxy8y90rbuz" style="display:inline"><span class="c58">Anchor text</span><span>&nbsp;</span></h3>
        </li>
    </ul>
    <ul class="c24 lst-kix_7wh80aky3tl-1 start">
        <li class="c6 li-bullet-0"><span class="c12 c44">Anchor text is the visible, clickable text of a link on a page.
                It is usually differentiated from the rest of the copy on the page by being a different colour, and is
                sometimes underlined.</span></li>
        <li class="c6 li-bullet-0"><span class="c4">The anchor text that is used as part of internal linking is
                important for providing context about the nature of the link and the page being linked to. Anchor text
                such as &ldquo;click here&rdquo; or &ldquo;discover more&rdquo; is poorly optimised anchor text as they
                provide no indication to users or search engines as to what the subject of the linked page is. Anchor
                text should ideally reflect the content of the linked page, ideally targeting the primary keyword of
                that page. For internal linking, we should try to utilise exact match, or partially matched anchor text,
                with exact match using the same keyword as the target page, and partial match using a variation of the
                keyword of the target page.</span></li>
        <li class="c6 li-bullet-0"><span class="c4">Care should be taken to ensure that anchor text isn&rsquo;t spammed
                however. The anchor text should be fairly concise, and not stuff keywords.</span></li>
    </ul>
    <h3 class="c1 c35" id="h.9ydfofs9k8rb"><span class="c47"></span></h3>
    <ul class="c24 lst-kix_7wh80aky3tl-0">
        <li class="c1 c43 li-bullet-0">
            <h3 id="h.es5gng2bgbyy" style="display:inline"><span class="c47">Parent or child pages &nbsp;</span></h3>
        </li>
    </ul>
    <ul class="c24 lst-kix_7wh80aky3tl-1 start">
        <li class="c6 li-bullet-0"><span class="c4">A parent page will likely target a &ldquo;head&rdquo; keyword, which
                is a broad keyword, which often has high monthly search volume, and is more competitive. An example
                might be &ldquo;disaster recovery&rdquo;. </span></li>
        <li class="c6 li-bullet-0"><span class="c4">A child page should support a parent page, and may target secondary
                keywords, or more long tail keywords. These are often more specific, lower volume and less competitive
                keywords. An example might be &ldquo;managed disaster recovery services&rdquo;.</span></li>
        <li class="c6 li-bullet-0"><span class="c4">This has implications on the internal linking of the page. Best
                practice for internal linking for parent and child pages is that parent pages will tend to have more
                internal links from across the rest of the site than a child page. This helps to indicate the hierarchy
                of our content, with the parent page as the more important page on our site, and the child pages
                supporting the parent page. Between parent and child pages, internal linking should reflect the full
                hierarchy of the content, with each child page linking to all parent pages above it in the hierarchy, as
                well as any sibling pages. A parent page should link through to its child pages, and any parent pages
                above it.</span></li>
        <li class="c6 li-bullet-0"><span class="c12">Not only does this help users navigate your content on the topic,
                it also helps to signal to search engines that this is a cluster of content that is closely related, and
                which is the most important parent content.</span></li>
    </ul>
    <h1 class="c0" id="h.up3qnogmnc91"><span class="c39">Other considerations</span></h1>
    <h3 class="c1" id="h.ecsrlmjf8amh"><span>Word count</span></h3>
    <p class="c15 c34"><span class="c4">In order to avoid the page being flagged as thin content, we must ensure the
            word count exceeds 300 words. Pages seen as thin content are considered to be low quality, and potentially
            spammy, and so are penalised in terms of rankings.</span></p>
    <p class="c15 c34"><span class="c12">Ultimately, the aim of our new content should be to answer the searcher&rsquo;s
            intent better than any of our competitors, so word count should not be our primary focus. While there are
            certainly some </span><span class="c21 c18"><a class="c2"
                href="https://www.google.com/url?q=https://backlinko.com/content-study&amp;sa=D&amp;source=editors&amp;ust=1692706675980453&amp;usg=AOvVaw1UoVjZGhlBg9LEL6QIfKvP">benefits
                of longer content</a></span><span class="c4">, our key goal should be on creating content that fulfils
            our core purpose, and is above the minimum threshold for thin content. </span></p>
    <p class="c15 c34"><span class="c4">Having said that, it can be useful to give an indication of word count for the
            content, to help signal whether this is a longer or shorter article. This can be used as a proxy to show how
            in depth the content will be, with higher word count content being more in depth. </span></p>
    <ul class="c24 lst-kix_kg1y8wqbxbmm-0 start">
        <li class="c10 li-bullet-0"><span class="c4">A short article will be 300-800 words</span></li>
        <li class="c10 li-bullet-0"><span class="c4">A medium length article will be 800-1600 words</span></li>
        <li class="c10 li-bullet-0"><span class="c12">A longer, more in depth article will exceed 1600 words</span></li>
    </ul>
    <h3 class="c1" id="h.ef496j5q1ah2"><span class="c9">Featured Snippets</span></h3>
    <p class="c15"><span class="c4">Featured snippets can be a good way of reaching a broader audience with a section of
            your content, without the user having to actually click into your page. This is great for building brand
            authority, and may encourage the user to click on your link, even if it&rsquo;s not the first ranked page on
            the SERP.</span></p>
    <p class="c15"><span class="c4">Not every search query has a featured snippet, so research should be carried out to
            see if there are any related to the primary and secondary keywords of the content. This can be done by
            replicating the searches on Google, or by using a tool such as SEMrush.</span></p>
    <p class="c15"><span class="c4">Typically, featured snippets appear more frequently for keywords queries containing
            more words. If there are featured snippets that we would want to target with our content, this should be
            reflected in the structure of that content.</span></p>
    <p class="c15"><span class="c21 c18"><a class="c2"
                href="https://www.google.com/url?q=https://www.semrush.com/blog/featured-snippet/?kw%3D%26cmp%3DUK_SRCH_DSA_Blog_Core_BU_EN%26label%3Ddsa_pagefeed%26Network%3Dg%26Device%3Dc%26utm_content%3D515816610887%26kwid%3Ddsa-1057183201835%26cmpid%3D11776881484%26agpid%3D113846055025%26BU%3DCore%26extid%3D167346300280%26adpos%3D%26gclid%3DCj0KCQjwub-HBhCyARIsAPctr7zUt11PQJDiYWCQRGksTerHawzFvUp8Yf0DxIvtKz9ixCXAqpJs2mAaApxJEALw_wcB&amp;sa=D&amp;source=editors&amp;ust=1692706675982558&amp;usg=AOvVaw2yHxFmEzcCKxfCYPzc567z">70%
                of featured snippets</a></span><span class="c12">&nbsp;are paragraphs of text, so the content of your
            site should aim to answer the queries with featured snippets in a concise and authoritative
            manner.</span><span class="c12">&nbsp;As stated above, the use of heading tags to form a question and answer
            format to address the topics you&rsquo;re targeting for a featured snippet is an effective
            method.</span><span class="c4">&nbsp;For example, the featured snippet for the query &ldquo;what is disaster
            recovery as a service&rdquo; is seen below:</span></p>
    <p class="c15"><span
            style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 161.33px;"><img
                alt="" src="images/image1.png"
                style="width: 601.70px; height: 161.33px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"
                title=""></span></p>
    <p class="c15"><span class="c4">On the VMware page, we can see that the H2 targets that exact search term, and the
            following text answers the question directly, and has subsequently been selected as the featured
            snippet.</span></p>
    <p class="c15"><span
            style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 108.00px;"><img
                alt="" src="images/image2.png"
                style="width: 601.70px; height: 108.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"
                title=""></span></p>
    <p class="c15"><span class="c4">The answer we provide in the new content has to be more effective at answering the
            question than the current featured snippet, e.g. more in depth, more accurate etc. &nbsp;</span></p>
    <h3 class="c1" id="h.ruuka4lir6uz"><span>Benchmark Content</span></h3>
    <p class="c15"><span class="c4">It is important that we are able to benchmark our content against similar or related
            content from competitors. We should identify a list of URLs from competitor domains that we can review, to
            make sure that our content is at least, if not better than, our competitors, and that we haven&rsquo;t
            missed any key areas in our new page.</span></p>
    <p class="c15"><span class="c4">Once the competitor URLs have been identified, and our content has been drafted, our
            content should be peer reviewed. Having a second or third pair of eyes read through the content and
            benchmark our new page against this checklist, as well as against the competitor URLs is an effective method
            of ensuring our content is well optimised before launch.</span></p>
    <p class="c15"><span class="c4">We can utilise the checklist above to see if the competitors have fully optimised
            their page, to help identify any gaps that we can ensure our page is optimised for.</span></p>
    <p class="c8 c32"><span class="c13"></span></p>
    <p class="c46 c32"><span class="c49 c55"></span></p>
    <div>
        <p class="c17 c53"><span class="c33 c30"></span></p>
        <p class="c53 c34"><span class="c30 c33">bluearray.co.uk &nbsp;| &nbsp;@bluearrayseo | 0800 0119 123</span></p>
        <p class="c32 c40"><span class="c30 c36"></span></p>
    </div>
    <div class="c41">
        <p class="c28"><a href="#cmnt_ref1" id="cmnt1">[a]</a><span class="c49 c54">we link to kw universe resource
                here</span></p>
    </div>
    <div class="c41">
        <p class="c28"><a href="#cmnt_ref2" id="cmnt2">[b]</a><span class="c54 c49">Specific to client</span></p>
    </div>
</body>

</html>
"""
new_parser.table_style = 'TableGrid'
new_parser.add_html_to_document(html, document)

# do more stuff to document
document.save('output_data.docx')