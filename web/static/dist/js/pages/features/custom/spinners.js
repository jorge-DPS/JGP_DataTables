"use strict";var KTSpinnersDemo={init:function(){var t,n,e,i;t=KTUtil.getById("kt_btn_1"),KTUtil.addEvent(t,"click",function(){KTUtil.btnWait(t,"spinner spinner-right spinner-white pr-15","Please wait"),setTimeout(function(){KTUtil.btnRelease(t)},1e3)}),n=KTUtil.getById("kt_btn_2"),KTUtil.addEvent(n,"click",function(){KTUtil.btnWait(n,"spinner spinner-dark spinner-right pr-15","Loading"),setTimeout(function(){KTUtil.btnRelease(n)},1e3)}),e=KTUtil.getById("kt_btn_3"),KTUtil.addEvent(e,"click",function(){KTUtil.btnWait(e,"spinner spinner-left spinner-darker-success pl-15","Disabled..."),setTimeout(function(){KTUtil.btnRelease(e)},1e3)}),i=KTUtil.getById("kt_btn_4"),KTUtil.addEvent(i,"click",function(){KTUtil.btnWait(i,"spinner spinner-left spinner-darker-danger pl-15","Please wait"),setTimeout(function(){KTUtil.btnRelease(i)},1e3)})}};jQuery(document).ready(function(){KTSpinnersDemo.init()});