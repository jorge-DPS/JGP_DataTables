!function(){"use strict";function o(e){return function(){return e}}var e=tinymce.util.Tools.resolve("tinymce.PluginManager"),u=function(){return(u=Object.assign||function(e){for(var t,r=1,n=arguments.length;r<n;r++)for(var i in t=arguments[r])Object.prototype.hasOwnProperty.call(t,i)&&(e[i]=t[i]);return e}).apply(this,arguments)},a=o(!1),c=o(!0),t=function(){return s},s={fold:function(e,t){return e()},is:a,isSome:a,isNone:c,getOr:i,getOrThunk:n,getOrDie:function(e){throw new Error(e||"error: getOrDie called on none.")},getOrNull:o(null),getOrUndefined:o(void 0),or:i,orThunk:n,map:t,each:function(){},bind:t,exists:a,forall:c,filter:t,equals:r,equals_:r,toArray:function(){return[]},toString:o("none()")};function r(e){return e.isNone()}function n(e){return e()}function i(e){return e}function l(e,t){for(var r=0,n=e.length;r<n;r++)t(e[r],r)}function d(e){var t=e;return{get:function(){return t},set:function(e){t=e}}}function m(e,t){return H(e,t)?R.from(e[t]):R.none()}function h(e){return e.getParam("media_scripts")}function f(e,t){if(e)for(var r=0;r<e.length;r++)if(-1!==t.indexOf(e[r].filter))return e[r]}function p(e){return e.replace(/px$/,"")}function g(i,e){var o=d(!1),a={};return K({validate:!1,allow_conditional_comments:!0,start:function(e,t){if(!o.get())if(H(t.map,"data-ephox-embed-iri"))o.set(!0),n=(n=(r=t).map.style)?Q.parseStyle(n):{},a={type:"ephox-embed-iri",source:r.map["data-ephox-embed-iri"],altsource:"",poster:"",width:m(n,"max-width").map(p).getOr(""),height:m(n,"max-height").map(p).getOr("")};else{if(a.source||"param"!==e||(a.source=t.map.movie),"iframe"!==e&&"object"!==e&&"embed"!==e&&"video"!==e&&"audio"!==e||(a.type||(a.type=e),a=J.extend(t.map,a)),"script"===e){n=f(i,t.map.src);if(!n)return;a={type:"script",source:t.map.src,width:String(n.width),height:String(n.height)}}"source"===e&&(a.source?a.altsource||(a.altsource=t.map.src):a.source=t.map.src),"img"!==e||a.poster||(a.poster=t.map.src)}var r,n}}).parse(e),a.source=a.source||a.src||a.data,a.altsource=a.altsource||"",a.poster=a.poster||"",a}function w(e){return(e={mp3:"audio/mpeg",m4a:"audio/x-m4a",wav:"audio/wav",mp4:"video/mp4",webm:"video/webm",ogg:"video/ogg",swf:"application/x-shockwave-flash"}[e.toLowerCase().split(".").pop()])||""}function v(e){return/^[0-9.]+$/.test(e)?e+"px":e}function b(o,e){!function(e,t){for(var r=W(e),n=0,i=r.length;n<i;n++){var o=r[n];t(e[o],o)}}(e,function(e,t){var r=""+e;if(o.map[t])for(var n=o.length;n--;){var i=o[n];i.name===t&&(r?(o.map[t]=r,i.value=r):(delete o.map[t],o.splice(n,1)))}else r&&(o.push({name:t,value:r}),o.map[t]=r)})}function y(e,a,c){var u,s=X(),l=d(!1),m=0;return K({validate:!1,allow_conditional_comments:!0,comment:function(e){s.comment(e)},cdata:function(e){s.cdata(e)},text:function(e,t){s.text(e,t)},start:function(e,t,r){if(!l.get())if(H(t.map,"data-ephox-embed-iri"))l.set(!0),n=a,(o=(o=(i=t).map.style)?Y.parseStyle(o):{})["max-width"]=v(n.width),o["max-height"]=v(n.height),b(i,{style:Y.serializeStyle(o)});else{switch(e){case"video":case"object":case"embed":case"img":case"iframe":void 0!==a.height&&void 0!==a.width&&b(t,{width:a.width,height:a.height})}if(c)switch(e){case"video":b(t,{poster:a.poster,src:""}),a.altsource&&b(t,{src:""});break;case"iframe":b(t,{src:a.source});break;case"source":if(m<2&&(b(t,{src:a[Z[m]],type:a[Z[m]+"mime"]}),!a[Z[m]]))return;m++;break;case"img":if(!a.poster)return;u=!0}}var n,i,o;s.start(e,t,r)},end:function(e){if(!l.get()){if("video"===e&&c)for(var t,r=0;r<2;r++)a[Z[r]]&&((t=[]).map={},m<=r&&(b(t,{src:a[Z[r]],type:a[Z[r]+"mime"]}),s.start("source",t,!0)));var n;a.poster&&"object"===e&&c&&!u&&((n=[]).map={},b(n,{src:a.poster,width:a.width,height:a.height}),s.start("img",n,!0))}s.end(e)}},V({})).parse(e),s.getContent()}function x(e,t){for(var r=function(e){e=e.match(/^(https?:\/\/|www\.)(.+)$/i);return!(e&&1<e.length)||"www."===e[1]?"https://":e[1]}(t),n=e.regex.exec(t),i=r+e.url,o=0;o<n.length;o++)!function(e){i=i.replace("$"+e,function(){return n[e]||""})}(o);return i.replace(/\?$/,"")}function j(r,e){var t,n=J.extend({},e);if(!n.source&&(J.extend(n,g(h(r),n.embed)),!n.source))return"";if(n.altsource||(n.altsource=""),n.poster||(n.poster=""),n.source=r.convertURL(n.source,"source"),n.altsource=r.convertURL(n.altsource,"source"),n.sourcemime=w(n.source),n.altsourcemime=w(n.altsource),n.poster=r.convertURL(n.poster,"poster"),(c=(t=n.source,0<(a=ee.filter(function(e){return e.regex.test(t)})).length?J.extend({},a[0],{url:x(a[0],t)}):null))&&(n.source=c.url,n.type=c.type,n.allowFullscreen=c.allowFullscreen,n.width=n.width||String(c.w),n.height=n.height||String(c.h)),n.embed)return y(n.embed,n,!0);(e=f(h(r),n.source))&&(n.type="script",n.width=String(e.width),n.height=String(e.height));var i,o,a=r.getParam("audio_template_callback"),c=r.getParam("video_template_callback");return n.width=n.width||"300",n.height=n.height||"150",J.each(n,function(e,t){n[t]=r.dom.encode(""+e)}),"iframe"===n.type?(o=n.allowFullscreen?' allowFullscreen="1"':"",'<iframe src="'+n.source+'" width="'+n.width+'" height="'+n.height+'"'+o+"></iframe>"):"application/x-shockwave-flash"===n.sourcemime?(o='<object data="'+(e=n).source+'" width="'+e.width+'" height="'+e.height+'" type="application/x-shockwave-flash">',e.poster&&(o+='<img src="'+e.poster+'" width="'+e.width+'" height="'+e.height+'" />'),o+="</object>"):-1!==n.sourcemime.indexOf("audio")?(i=n,(a=a)?a(i):'<audio controls="controls" src="'+i.source+'">'+(i.altsource?'\n<source src="'+i.altsource+'"'+(i.altsourcemime?' type="'+i.altsourcemime+'"':"")+" />\n":"")+"</audio>"):"script"===n.type?'<script src="'+n.source+'"><\/script>':(i=n,(c=c)?c(i):'<video width="'+i.width+'" height="'+i.height+'"'+(i.poster?' poster="'+i.poster+'"':"")+' controls="controls">\n<source src="'+i.source+'"'+(i.sourcemime?' type="'+i.sourcemime+'"':"")+" />\n"+(i.altsource?'<source src="'+i.altsource+'"'+(i.altsourcemime?' type="'+i.altsourcemime+'"':"")+" />\n":"")+"</video>")}function O(n,i,o){return new te(function(t,e){function r(e){return e.html&&(re[n.source]=e),t({url:n.source,html:e.html||i(n)})}re[n.source]?r(re[n.source]):o({url:n.source},r,e)})}function S(t){return function(e){return j(t,e)}}function _(e,t){var r,n,i=e.getParam("media_url_resolver");return i?O(t,S(e),i):(r=t,n=S(e),new te(function(e){e({html:n(r),url:r.source})}))}function k(o,a,c){return function(e){function t(){return m(o,e)}function r(){return m(a,e)}function n(e){return m(e,"value").bind(function(e){return 0<e.length?R.some(e):R.none()})}var i={};return i[e]=(e===c?t().bind(function(e){return I(e)?n(e).orThunk(r):r().orThunk(function(){return R.from(e)})}):r().orThunk(function(){return t().bind(function(e){return I(e)?n(e):R.from(e)})})).getOr(""),i}}function A(e,t){var r,n,i=t?m(e,t).bind(function(e){return m(e,"meta")}).getOr({}):{},t=k(e,i,t);return u(u(u(u(u({},t("source")),t("altsource")),t("poster")),t("embed")),(r=i,n={},m(e,"dimensions").each(function(e){l(["width","height"],function(t){m(r,t).orThunk(function(){return m(e,t)}).each(function(e){return n[t]=e})})}),n))}function T(e){var n=u(u({},e),{source:{value:m(e,"source").getOr("")},altsource:{value:m(e,"altsource").getOr("")},poster:{value:m(e,"poster").getOr("")}});return l(["width","height"],function(r){m(e,r).each(function(e){var t=n.dimensions||{};t[r]=e,n.dimensions=t})}),n}function C(t){return function(e){e=e&&e.msg?"Media embed handler error: "+e.msg:"Media embed handler threw unknown error.";t.notificationManager.open({type:"error",text:e})}}function P(e,t){return g(h(e),t)}function D(n,i){return function(e){var t,r;L(e.url)&&0<e.url.trim().length&&(r=e.html,t=P(i,r),r=u(u({},t),{source:e.url,embed:r}),n.setData(T(r)))}}function $(e,t){var r=e.dom.select("img[data-mce-object]");e.insertContent(t),function(e,t){for(var r=e.dom.select("img[data-mce-object]"),n=0;n<t.length;n++)for(var i=r.length-1;0<=i;i--)t[n]===r[i]&&r.splice(i,1);e.selection.select(r[0])}(e,r),e.nodeChanged()}function F(e,t,r){t.embed=y(t.embed,t),t.embed&&(e.source===t.source||(e=t.source,re.hasOwnProperty(e)))?$(r,t.embed):_(r,t).then(function(e){$(r,e.html)}).catch(C(r))}function M(o){var e=(n=(r=o).selection.getNode(),n=(t=n).getAttribute("data-mce-object")||t.getAttribute("data-ephox-embed-iri")?r.serializer.serialize(n,{selection:!0}):"",u({embed:n},g(h(r),n))),a=d(e),t=T(e),r={title:"General",name:"general",items:function(e){for(var t=[],r=0,n=e.length;r<n;++r){if(!q(e[r]))throw new Error("Arr.flatten item "+r+" was not an array, input: "+e);B.apply(t,e[r])}return t}([[{name:"source",type:"urlinput",filetype:"media",label:"Source"}],o.getParam("media_dimensions",!0)?[{type:"sizeinput",name:"dimensions",label:"Constrain proportions",constrain:!0}]:[]])},n={title:"Embed",items:[{type:"textarea",name:"embed",label:"Paste your embed code below:"}]},e=[];o.getParam("media_alt_source",!0)&&e.push({name:"altsource",type:"urlinput",filetype:"media",label:"Alternative source URL"}),o.getParam("media_poster",!0)&&e.push({name:"poster",type:"urlinput",filetype:"image",label:"Media poster (Image URL)"}),n=[r,n],0<e.length&&n.push({title:"Advanced",name:"advanced",items:e});var c=o.windowManager.open({title:"Insert/Edit Media",size:"normal",body:{type:"tabpanel",tabs:n},buttons:[{type:"cancel",name:"cancel",text:"Cancel"},{type:"submit",name:"save",text:"Save",primary:!0}],onSubmit:function(e){var t=A(e.getData());F(a.get(),t,o),e.close()},onChange:function(e,t){switch(t.name){case"source":!function(e,t){t=A(t.getData(),"source");e.source!==t.source&&(D(c,o)({url:t.source,html:""}),_(o,t).then(D(c,o)).catch(C(o)))}(a.get(),e);break;case"embed":i=A((n=e).getData()),i=P(o,i.embed),n.setData(T(i));break;case"dimensions":case"altsource":case"poster":r=e,n=t.name,i=A(r.getData(),n),n=j(o,i),r.setData(T(u(u({},i),{embed:n})))}var r,n,i;a.set(A(e.getData()))},initialData:t})}function z(o,e){if(!1===o.getParam("media_filter_html",!0))return e;var a,c=X();return K({validate:!1,allow_conditional_comments:!1,comment:function(e){c.comment(e)},cdata:function(e){c.cdata(e)},text:function(e,t){c.text(e,t)},start:function(e,t,r){if(a=!0,"script"!==e&&"noscript"!==e&&"svg"!==e){for(var n=t.length-1;0<=n;n--){var i=t[n].name;0===i.indexOf("on")&&(delete t.map[i],t.splice(n,1)),"style"===i&&(t[n].value=o.dom.serializeStyle(o.dom.parseStyle(t[n].value),e))}c.start(e,t,r),a=!1}},end:function(e){a||c.end(e)}},V({})).parse(e),c.getContent()}function N(e){for(;e=e.parent;)if(e.attr("data-ephox-embed-iri")||function(e){e=e.attr("class");return e&&/\btiny-pageembed\b/.test(e)}(e))return 1}function U(c){return function(e){for(var t,r,n,i,o,a=e.length;a--;)(n=e[a]).parent&&(n.parent.attr("data-mce-object")||"script"===n.name&&!(t=f(h(c),n.attr("src")))||(t&&(t.width&&n.attr("width",t.width.toString()),t.height&&n.attr("height",t.height.toString())),"iframe"===n.name&&c.getParam("media_live_embeds",!0)&&ie.ceFalse?N(n)||n.replace(function(e,t){var r=t.name,n=new ne("span",1);n.attr({contentEditable:"false",style:t.attr("style"),"data-mce-object":r,class:"mce-preview-object mce-object-"+r}),oe(e,t,n);r=new ne(r,1);r.attr({src:t.attr("src"),allowfullscreen:t.attr("allowfullscreen"),style:t.attr("style"),class:t.attr("class"),width:t.attr("width"),height:t.attr("height"),frameborder:"0"});t=new ne("span",1);return t.attr("class","mce-shim"),n.append(r),n.append(t),n}(c,n)):N(n)||n.replace((r=c,o=i=void 0,i=(n=n).name,(o=new ne("img",1)).shortEnded=!0,oe(r,n,o),o.attr({width:n.attr("width")||"300",height:n.attr("height")||("audio"===i?"30":"150"),style:n.attr("style"),src:ie.transparentSrc,"data-mce-object":i,class:"mce-object mce-object-"+i}),o))))}}var E=function(r){function e(){return i}function t(e){return e(r)}var n=o(r),i={fold:function(e,t){return t(r)},is:function(e){return r===e},isSome:c,isNone:a,getOr:n,getOrThunk:n,getOrDie:n,getOrNull:n,getOrUndefined:n,or:e,orThunk:e,map:function(e){return E(e(r))},each:function(e){e(r)},bind:t,exists:t,forall:t,filter:function(e){return e(r)?i:s},toArray:function(){return[r]},toString:function(){return"some("+r+")"},equals:function(e){return e.is(r)},equals_:function(e,t){return e.fold(a,function(e){return t(r,e)})}};return i},R={some:E,none:t,from:function(e){return null==e?s:E(e)}},t=function(r){return function(e){return e=typeof(t=e),(null===t?"null":"object"==e&&(Array.prototype.isPrototypeOf(t)||t.constructor&&"Array"===t.constructor.name)?"array":"object"==e&&(String.prototype.isPrototypeOf(t)||t.constructor&&"String"===t.constructor.name)?"string":e)===r;var t}},L=t("string"),I=t("object"),q=t("array"),B=Array.prototype.push,W=Object.keys,G=Object.hasOwnProperty,H=function(e,t){return G.call(e,t)},J=tinymce.util.Tools.resolve("tinymce.util.Tools"),t=tinymce.util.Tools.resolve("tinymce.dom.DOMUtils"),K=tinymce.util.Tools.resolve("tinymce.html.SaxParser"),Q=t.DOM,V=tinymce.util.Tools.resolve("tinymce.html.Schema"),X=tinymce.util.Tools.resolve("tinymce.html.Writer"),Y=t.DOM,Z=["source","altsource"],ee=[{regex:/youtu\.be\/([\w\-_\?&=.]+)/i,type:"iframe",w:560,h:314,url:"www.youtube.com/embed/$1",allowFullscreen:!0},{regex:/youtube\.com(.+)v=([^&]+)(&([a-z0-9&=\-_]+))?/i,type:"iframe",w:560,h:314,url:"www.youtube.com/embed/$2?$4",allowFullscreen:!0},{regex:/youtube.com\/embed\/([a-z0-9\?&=\-_]+)/i,type:"iframe",w:560,h:314,url:"www.youtube.com/embed/$1",allowFullscreen:!0},{regex:/vimeo\.com\/([0-9]+)/,type:"iframe",w:425,h:350,url:"player.vimeo.com/video/$1?title=0&byline=0&portrait=0&color=8dc7dc",allowFullscreen:!0},{regex:/vimeo\.com\/(.*)\/([0-9]+)/,type:"iframe",w:425,h:350,url:"player.vimeo.com/video/$2?title=0&amp;byline=0",allowFullscreen:!0},{regex:/maps\.google\.([a-z]{2,3})\/maps\/(.+)msid=(.+)/,type:"iframe",w:425,h:350,url:'maps.google.com/maps/ms?msid=$2&output=embed"',allowFullscreen:!1},{regex:/dailymotion\.com\/video\/([^_]+)/,type:"iframe",w:480,h:270,url:"www.dailymotion.com/embed/video/$1",allowFullscreen:!0},{regex:/dai\.ly\/([^_]+)/,type:"iframe",w:480,h:270,url:"www.dailymotion.com/embed/video/$1",allowFullscreen:!0}],te=tinymce.util.Tools.resolve("tinymce.util.Promise"),re={},ne=tinymce.util.Tools.resolve("tinymce.html.Node"),ie=tinymce.util.Tools.resolve("tinymce.Env"),oe=function(e,t,r){for(var n,i,o=t.attributes,a=o.length;a--;)n=o[a].name,i=o[a].value,"width"!==n&&"height"!==n&&"style"!==n&&("data"!==n&&"src"!==n||(i=e.convertURL(i,n)),r.attr("data-mce-p-"+n,i));t=t.firstChild&&t.firstChild.value;t&&(r.attr("data-mce-html",escape(z(e,t))),r.firstChild=null)};e.add("media",function(e){var t,r,n,i,l,o,a;return(t=e).addCommand("mceMedia",function(){M(t)}),(r=e).ui.registry.addToggleButton("media",{tooltip:"Insert/edit media",icon:"embed",onAction:function(){r.execCommand("mceMedia")},onSetup:(n=r,i=["img[data-mce-object]","span[data-mce-object]","div[data-ephox-embed-iri]"],function(e){return n.selection.selectorChangedWithUnbind(i.join(","),e.setActive).unbind})}),r.ui.registry.addMenuItem("media",{icon:"embed",text:"Media...",onAction:function(){r.execCommand("mceMedia")}}),e.on("ResolveName",function(e){var t;1===e.target.nodeType&&(t=e.target.getAttribute("data-mce-object"))&&(e.name=t)}),(l=e).on("preInit",function(){var t=l.schema.getSpecialElements();J.each("video audio iframe object".split(" "),function(e){t[e]=new RegExp("</"+e+"[^>]*>","gi")});var r=l.schema.getBoolAttrs();J.each("webkitallowfullscreen mozallowfullscreen allowfullscreen".split(" "),function(e){r[e]={}}),l.parser.addNodeFilter("iframe,video,audio,object,embed,script",U(l)),l.serializer.addAttributeFilter("data-mce-object",function(e,t){for(var r,n,i,o,a,c,u=e.length;u--;)if((r=e[u]).parent){for(a=r.attr(t),n=new ne(a,1),"audio"!==a&&"script"!==a&&((c=r.attr("class"))&&-1!==c.indexOf("mce-preview-object")?n.attr({width:r.firstChild.attr("width"),height:r.firstChild.attr("height")}):n.attr({width:r.attr("width"),height:r.attr("height")})),n.attr({style:r.attr("style")}),i=(o=r.attributes).length;i--;){var s=o[i].name;0===s.indexOf("data-mce-p-")&&n.attr(s.substr(11),o[i].value)}"script"===a&&n.attr("type","text/javascript"),(c=r.attr("data-mce-html"))&&((a=new ne("#text",3)).raw=!0,a.value=z(l,unescape(c)),n.append(a)),r.replace(n)}})}),l.on("SetContent",function(){l.$("span.mce-preview-object").each(function(e,t){t=l.$(t);0===t.find("span.mce-shim").length&&t.append('<span class="mce-shim"></span>')})}),(o=e).on("click keyup touchend",function(){var e=o.selection.getNode();e&&o.dom.hasClass(e,"mce-preview-object")&&o.dom.getAttrib(e,"data-mce-selected")&&e.setAttribute("data-mce-selected","2")}),o.on("ObjectSelected",function(e){var t=e.target.getAttribute("data-mce-object");"audio"!==t&&"script"!==t||e.preventDefault()}),o.on("ObjectResized",function(e){var t,r=e.target;r.getAttribute("data-mce-object")&&(t=r.getAttribute("data-mce-html"))&&(t=unescape(t),r.setAttribute("data-mce-html",escape(y(t,{width:String(e.width),height:String(e.height)}))))}),a=e,{showDialog:function(){M(a)}}})}();