!function(){"use strict";var t=tinymce.util.Tools.resolve("tinymce.PluginManager"),i=function(){return(i=Object.assign||function(t){for(var n,r=1,e=arguments.length;r<e;r++)for(var o in n=arguments[r])Object.prototype.hasOwnProperty.call(n,o)&&(t[o]=n[o]);return t}).apply(this,arguments)};function n(){}function a(t){return function(){return t}}function e(t){return t}var u=a(!1),f=a(!0),r=function(){return c},c={fold:function(t,n){return t()},is:u,isSome:u,isNone:f,getOr:l,getOrThunk:s,getOrDie:function(t){throw new Error(t||"error: getOrDie called on none.")},getOrNull:a(null),getOrUndefined:a(void 0),or:l,orThunk:s,map:r,each:n,bind:r,exists:u,forall:f,filter:r,equals:o,equals_:o,toArray:function(){return[]},toString:a("none()")};function o(t){return t.isNone()}function s(t){return t()}function l(t){return t}function d(t,n){return-1<st.call(t,n)}function m(t,n){for(var r=t.length,e=new Array(r),o=0;o<r;o++){var a=t[o];e[o]=n(a,o)}return e}function g(t,n){for(var r=0,e=t.length;r<e;r++)n(t[r],r)}function p(t,n){for(var r=[],e=0,o=t.length;e<o;e++){var a=t[e];n(a,e)&&r.push(a)}return r}function h(t,n,r){return function(t,n){for(var r=t.length-1;0<=r;r--)n(t[r],r)}(t,function(t){r=n(r,t)}),r}function v(t,n){return function(t,n,r){for(var e=0,o=t.length;e<o;e++){var a=t[e];if(n(a,e))return at.some(a);if(r(a,e))break}return at.none()}(t,n,u)}function y(t,n){for(var r=0,e=t.length;r<e;++r)if(!0!==n(t[r],r))return!1;return!0}function b(t){return n=t,(t=0)<=t&&t<n.length?at.some(n[t]):at.none();var n}function k(t){var n=[],r=[];return g(t,function(t){t.fold(function(t){n.push(t)},function(t){r.push(t)})}),{errors:n,values:r}}function O(t){return"inline-command"===t.type||"inline-format"===t.type}function w(t){return"block-command"===t.type||"block-format"===t.type}function C(t){return function(t,n){t=ct.call(t,0);return t.sort(n),t}(t,function(t,n){return t.start.length===n.start.length?0:t.start.length>n.start.length?-1:1})}function E(e){function o(t){return pt.error({message:t,pattern:e})}function t(t,n,r){if(void 0===e.format)return void 0!==e.cmd?it(e.cmd)?pt.value(r(e.cmd,e.value)):o(t+" pattern has non-string `cmd` parameter"):o(t+" pattern is missing both `format` and `cmd` parameters");if(r=void 0,ft(e.format)){if(!y(e.format,it))return o(t+" pattern has non-string items in the `format` array");r=e.format}else{if(!it(e.format))return o(t+" pattern has non-string `format` parameter");r=[e.format]}return pt.value(n(r))}if(!ut(e))return o("Raw pattern is not an object");if(!it(e.start))return o("Raw pattern is missing `start` parameter");if(void 0===e.end)return void 0!==e.replacement?it(e.replacement)?0===e.start.length?o("Replacement pattern has empty `start` parameter"):pt.value({type:"inline-command",start:"",end:e.start,cmd:"mceInsertContent",value:e.replacement}):o("Replacement pattern has non-string `replacement` parameter"):0===e.start.length?o("Block pattern has empty `start` parameter"):t("Block",function(t){return{type:"block-format",start:e.start,format:t[0]}},function(t,n){return{type:"block-command",start:e.start,cmd:t,value:n}});if(!it(e.end))return o("Inline pattern has non-string `end` parameter");if(0===e.start.length&&0===e.end.length)return o("Inline pattern has empty `start` and `end` parameters");var r=e.start,a=e.end;return 0===a.length&&(a=r,r=""),t("Inline",function(t){return{type:"inline-format",start:r,end:a,format:t}},function(t,n){return{type:"inline-command",start:r,end:a,cmd:t,value:n}})}function x(t){return"block-command"===t.type?{start:t.start,cmd:t.cmd,value:t.value}:"block-format"===t.type?{start:t.start,format:t.format}:"inline-command"===t.type?"mceInsertContent"===t.cmd&&""===t.start?{start:t.end,replacement:t.value}:{start:t.start,end:t.end,cmd:t.cmd,value:t.value}:"inline-format"===t.type?{start:t.start,end:t.end,format:1===t.format.length?t.format[0]:t.format}:void 0}function R(t){return{inlinePatterns:p(t,O),blockPatterns:C(p(t,w))}}function T(r){return{setPatterns:function(t){var n=k(m(t,E));if(0<n.errors.length){t=n.errors[0];throw new Error(t.message+":\n"+JSON.stringify(t.pattern,null,2))}r.set(R(n.values))},getPatterns:function(){return function(){for(var t=0,n=0,r=arguments.length;n<r;n++)t+=arguments[n].length;for(var e=Array(t),o=0,n=0;n<r;n++)for(var a=arguments[n],i=0,u=a.length;i<u;i++,o++)e[o]=a[i];return e}(m(r.get().inlinePatterns,x),m(r.get().blockPatterns,x))}}}function N(){for(var t=[],n=0;n<arguments.length;n++)t[n]=arguments[n];var r=ht.console;r&&(r.error||r.log).apply(r,t)}function P(t){return!1===(t=t.getParam("forced_root_block","p"))?"":!0===t?"p":t}function S(t,n){return{container:t,offset:n}}function M(t){return t.nodeType===Node.TEXT_NODE}function A(t,n,r,e){void 0===e&&(e=!0);var o=n.startContainer.parentNode,a=n.endContainer.parentNode;n.deleteContents(),e&&!r(n.startContainer)&&(M(n.startContainer)&&0===n.startContainer.data.length&&t.remove(n.startContainer),M(n.endContainer)&&0===n.endContainer.data.length&&t.remove(n.endContainer),wt(t,o,r),o!==a&&wt(t,a,r))}function B(t,n){return t=n.get(t),ft(t)&&b(t).exists(function(t){return n="block",dt.call(t,n);var n})}function D(t){return 0===t.start.length}function I(t,n){return n=at.from(t.dom.getParent(n.startContainer,t.dom.isBlock)),""===P(t)?n.orThunk(function(){return at.some(t.getBody())}):n}function j(n){return function(t){return n===t?-1:0}}function _(t,n,r){if(M(t)&&0<=n)return at.some(S(t,n));var e=Ot(Ct);return at.from(e.backwards(t,n,j(t),r)).map(function(t){return S(t.container,t.container.data.length)})}function U(t,n,r,e,o){var a,t=Ot(t,(a=t,function(t){return a.isBlock(t)||d(["BR","IMG","HR","INPUT"],t.nodeName)||"false"===a.getContentEditable(t)}));return at.from(t.backwards(n,r,e,o))}function q(t,n,r){if(M(n)&&(r<0||r>n.data.length))return[];for(var e=[r],o=n;o!==t&&o.parentNode;){for(var a=o.parentNode,i=0;i<a.childNodes.length;i++)if(a.childNodes[i]===o){e.push(i);break}o=a}return o===t?e.reverse():[]}function L(t,n,r,e,o){return{start:q(t,n,r),end:q(t,e,o)}}function V(t,n){var r,e,o=(n=n.slice()).pop();return(n=n,r=function(t,n){return t.bind(function(t){return at.from(t.childNodes[n])})},e=at.some(t),g(n,function(t){e=r(e,t)}),e).bind(function(t){return M(t)&&(o<0||o>t.data.length)?at.none():at.some({node:t,offset:o})})}function W(n,r){return V(n,r.start).bind(function(t){var e=t.node,o=t.offset;return V(n,r.end).map(function(t){var n=t.node,r=t.offset,t=document.createRange();return t.setStart(e,o),t.setEnd(n,r),t})})}function F(e,o,n){(function(t,n,r){if(M(t)&&n>=t.length)return at.some(S(t,n));var e=Ot(Ct);return at.from(e.forwards(t,n,j(t),r)).map(function(t){return S(t.container,0)})})(o,0,o).each(function(t){var r=t.container;xt(r,n.start.length,o).each(function(t){var n=e.createRng();n.setStart(r,0),n.setEnd(t.container,t.offset),A(e,n,function(t){return t===o})})})}function G(r,a){var i=r.dom,t=r.selection.getRng();return I(r,t).filter(function(t){var n=P(r),n=""===n&&i.is(t,"body")||i.is(t,n);return null!==t&&n}).bind(function(n){var t,r,e,o=n.textContent;return(t=a,e=(r=o).replace(" "," "),v(t,function(t){return 0===r.indexOf(t.start)||0===e.indexOf(t.start)})).map(function(t){return kt.trim(o).length===t.start.length?[]:[{pattern:t,range:L(i.getRoot(),n,0,n,0)}]})}).getOr([])}function H(o,t){var n;0!==t.length&&(n=o.selection.getBookmark(),g(t,function(t){return r=t,t=(n=o).dom,e=r.pattern,r=W(t.getRoot(),r.range).getOrDie("Unable to resolve path range"),I(n,r).each(function(t){"block-format"===e.type?B(e.format,n.formatter)&&n.undoManager.transact(function(){F(n.dom,t,e),n.formatter.apply(e.format)}):"block-command"===e.type&&n.undoManager.transact(function(){F(n.dom,t,e),n.execCommand(e.cmd,!1,e.value)})}),!0;var n,r,e}),o.selection.moveToBookmark(n))}function J(t,n){return t.create("span",{"data-mce-type":"bookmark",id:n})}function K(t,n){return(t=t.createRng()).setStartAfter(n.start),t.setEndBefore(n.end),t}function X(t,n,r){var e=(o=W(t.getRoot(),r).getOrDie("Unable to resolve path range")).startContainer,r=o.endContainer,r=0===o.endOffset?r:r.splitText(o.endOffset),o=0===o.startOffset?e:e.splitText(o.startOffset);return{prefix:n,end:r.parentNode.insertBefore(J(t,n+"-end"),r),start:o.parentNode.insertBefore(J(t,n+"-start"),o)}}function z(t,n,r){wt(t,t.get(n.prefix+"-end"),r),wt(t,t.get(n.prefix+"-start"),r)}function Q(o,a,i){var u=o.dom,f=u.getRoot(),c=i.pattern,s=i.position.container,l=i.position.offset;return Et(s,l-i.pattern.end.length,a).bind(function(t){var r=L(f,t.container,t.offset,s,l);if(D(c))return at.some({matches:[{pattern:c,startRng:r,endRng:r}],position:t});var n=Nt(o,i.remainingPatterns,t.container,t.offset,a),e=n.getOr({matches:[],position:t}),t=e.position;return function(t,r,n,e,o,a){if(void 0===a&&(a=!1),0!==r.start.length||a)return _(n,e,o).bind(function(n){return Tt(t,r,o,n).bind(function(t){if(a){if(t.endContainer===n.container&&t.endOffset===n.offset)return at.none();if(0===n.offset&&t.endContainer.textContent.length===t.endOffset)return at.none()}return at.some(t)})});var i=t.createRng();return i.setStart(n,e),i.setEnd(n,e),at.some(i)}(u,c,t.container,t.offset,a,n.isNone()).map(function(t){var n=L(f,t.startContainer,t.startOffset,t.endContainer,t.endOffset);return{matches:e.matches.concat([{pattern:c,startRng:n,endRng:r}]),position:S(t.startContainer,t.startOffset)}})})}function Y(n,t,r){n.selection.setRng(r),"inline-format"===t.type?g(t.format,function(t){n.formatter.apply(t)}):n.execCommand(t.cmd,!1,t.value)}function Z(e,t){var n,r,o=(n="mce_textpattern",r=(new Date).getTime(),n+"_"+Math.floor(1e9*Math.random())+ ++Rt+String(r)),a=h(t,function(t,n){var r=X(e,o+"_end"+t.length,n.endRng);return t.concat([i(i({},n),{endMarker:r})])},[]);return h(a,function(t,n){var r=a.length-t.length-1,r=D(n.pattern)?n.endMarker:X(e,o+"_start"+r,n.startRng);return t.concat([i(i({},n),{startMarker:r})])},[])}function $(r,e,o){var a=r.selection.getRng();return!1===a.collapsed?[]:I(r,a).bind(function(t){var n=a.startOffset-(o?1:0);return Nt(r,e,a.startContainer,n,t)}).fold(function(){return[]},function(t){return t.matches})}function tt(e,t){var o,n;0!==t.length&&(o=e.dom,n=e.selection.getBookmark(),t=Z(o,t),g(t,function(t){function n(t){return t===r}var r=o.getParent(t.startMarker.start,o.isBlock);D(t.pattern)?function(t,n,r,e){r=K(t.dom,r);A(t.dom,r,e),Y(t,n,r)}(e,t.pattern,t.endMarker,n):function(t,n,r,e,o){var a=t.dom,i=K(a,e),u=K(a,r);A(a,u,o),A(a,i,o);e={prefix:r.prefix,start:r.end,end:e.start},e=K(a,e);Y(t,n,e)}(e,t.pattern,t.startMarker,t.endMarker,n),z(o,t.endMarker,n),z(o,t.startMarker,n)}),e.selection.moveToBookmark(n))}function nt(t,n){var r=$(t,n.inlinePatterns,!0);0<r.length&&t.undoManager.transact(function(){tt(t,r)})}function rt(t,n,r){for(var e=0;e<t.length;e++)if(r(t[e],n))return!0}function et(n,r){var e=[",",".",";",":","!","?"],o=[32];n.on("keydown",function(t){13!==t.keyCode||bt.modifierPressed(t)||!function(r,t){if(!r.selection.isCollapsed())return!1;var n=$(r,t.inlinePatterns,!1),e=G(r,t.blockPatterns);return(0<e.length||0<n.length)&&(r.undoManager.add(),r.undoManager.extra(function(){r.execCommand("mceInsertNewLine")},function(){r.insertContent("\ufeff"),tt(r,n),H(r,e);var t=r.selection.getRng(),t=_(t.startContainer,t.startOffset,r.dom.getRoot());r.execCommand("mceInsertNewLine"),t.each(function(t){var n=t.container;"\ufeff"===n.data.charAt(t.offset-1)&&(n.deleteData(t.offset-1,1),wt(r.dom,n.parentNode,function(t){return t===r.dom.getRoot()}))})}),!0)}(n,r.get())||t.preventDefault()},!0),n.on("keyup",function(t){rt(o,t,function(t,n){return t===n.keyCode&&!1===bt.modifierPressed(n)})&&nt(n,r.get())}),n.on("keypress",function(t){rt(e,t,function(t,n){return t.charCodeAt(0)===n.charCode})&&yt.setEditorTimeout(n,function(){nt(n,r.get())})})}var ot=function(r){function t(){return o}function n(t){return t(r)}var e=a(r),o={fold:function(t,n){return n(r)},is:function(t){return r===t},isSome:f,isNone:u,getOr:e,getOrThunk:e,getOrDie:e,getOrNull:e,getOrUndefined:e,or:t,orThunk:t,map:function(t){return ot(t(r))},each:function(t){t(r)},bind:n,exists:n,forall:n,filter:function(t){return t(r)?o:c},toArray:function(){return[r]},toString:function(){return"some("+r+")"},equals:function(t){return t.is(r)},equals_:function(t,n){return t.fold(u,function(t){return n(r,t)})}};return o},at={some:ot,none:r,from:function(t){return null==t?c:ot(t)}},r=function(r){return function(t){return t=typeof(n=t),(null===n?"null":"object"==t&&(Array.prototype.isPrototypeOf(n)||n.constructor&&"Array"===n.constructor.name)?"array":"object"==t&&(String.prototype.isPrototypeOf(n)||n.constructor&&"String"===n.constructor.name)?"string":t)===r;var n}},it=r("string"),ut=r("object"),ft=r("array"),ct=Array.prototype.slice,st=Array.prototype.indexOf,lt=Object.keys,dt=Object.hasOwnProperty,mt=(function(i){if(!ft(i))throw new Error("cases must be an array");if(0===i.length)throw new Error("there must be at least one case");var u=[],r={};g(i,function(t,e){var n=lt(t);if(1!==n.length)throw new Error("one and only one name per case");var o=n[0],a=t[o];if(void 0!==r[o])throw new Error("duplicate key detected:"+o);if("cata"===o)throw new Error("cannot have a case named cata (sorry)");if(!ft(a))throw new Error("case arguments must be an array");u.push(o),r[o]=function(){var t=arguments.length;if(t!==a.length)throw new Error("Wrong number of arguments to case "+o+". Expected "+a.length+" ("+a+"), got "+t);for(var r=new Array(t),n=0;n<r.length;n++)r[n]=arguments[n];return{fold:function(){if(arguments.length!==i.length)throw new Error("Wrong number of arguments to fold. Expected "+i.length+", got "+arguments.length);return arguments[e].apply(null,r)},match:function(t){var n=lt(t);if(u.length!==n.length)throw new Error("Wrong number of arguments to match. Expected: "+u.join(",")+"\nActual: "+n.join(","));if(!y(u,function(t){return d(n,t)}))throw new Error("Not all branches were specified when using match. Specified: "+n.join(", ")+"\nRequired: "+u.join(", "));return t[o].apply(null,r)},log:function(t){console.log(t,{constructors:u,constructor:o,params:r})}}}})}([{bothErrors:["error1","error2"]},{firstError:["error1","value2"]},{secondError:["value1","error2"]},{bothValues:["value1","value2"]}]),function(r){return{is:function(t){return r===t},isValue:f,isError:u,getOr:a(r),getOrThunk:a(r),getOrDie:a(r),or:function(t){return mt(r)},orThunk:function(t){return mt(r)},fold:function(t,n){return n(r)},map:function(t){return mt(t(r))},mapError:function(t){return mt(r)},each:function(t){t(r)},bind:function(t){return t(r)},exists:function(t){return t(r)},forall:function(t){return t(r)},toOptional:function(){return at.some(r)}}}),gt=function(r){return{is:u,isValue:u,isError:f,getOr:e,getOrThunk:function(t){return t()},getOrDie:function(){return t=String(r),function(){throw new Error(t)}();var t},or:function(t){return t},orThunk:function(t){return t()},fold:function(t,n){return t(r)},map:function(t){return gt(r)},mapError:function(t){return gt(t(r))},each:n,bind:function(t){return gt(r)},exists:u,forall:f,toOptional:at.none}},pt={value:mt,error:gt,fromOption:function(t,n){return t.fold(function(){return gt(n)},mt)}},ht="undefined"!=typeof window?window:Function("return this;")(),vt=[{start:"*",end:"*",format:"italic"},{start:"**",end:"**",format:"bold"},{start:"#",format:"h1"},{start:"##",format:"h2"},{start:"###",format:"h3"},{start:"####",format:"h4"},{start:"#####",format:"h5"},{start:"######",format:"h6"},{start:"1. ",cmd:"InsertOrderedList"},{start:"* ",cmd:"InsertUnorderedList"},{start:"- ",cmd:"InsertUnorderedList"}],yt=tinymce.util.Tools.resolve("tinymce.util.Delay"),bt=tinymce.util.Tools.resolve("tinymce.util.VK"),kt=tinymce.util.Tools.resolve("tinymce.util.Tools"),r=tinymce.util.Tools.resolve("tinymce.dom.DOMUtils"),Ot=tinymce.util.Tools.resolve("tinymce.dom.TextSeeker"),wt=function(t,n,r){var e;n&&t.isEmpty(n)&&!r(n)&&(e=n.parentNode,t.remove(n),wt(t,e,r))},Ct=r.DOM,Et=function(t,r,e){if(!M(t))return at.none();var n=t.textContent;if(0<=r&&r<=n.length)return at.some(S(t,r));n=Ot(Ct);return at.from(n.backwards(t,r,j(t),e)).bind(function(t){var n=t.container.data;return Et(t.container,r+n.length,e)})},xt=function(t,n,r){if(!M(t))return at.none();var e=t.textContent;if(n<=e.length)return at.some(S(t,n));var o=Ot(Ct);return at.from(o.forwards(t,n,j(t),r)).bind(function(t){return xt(t.container,n-e.length,r)})},Rt=0,Tt=function(e,n,o,t){var r,a=n.start;return U(e,t.container,t.offset,(r=a,function(t,n){t=t.data.substring(0,n),n=t.lastIndexOf(r.charAt(r.length-1)),t=t.lastIndexOf(r);return-1!==t?t+r.length:-1!==n?n+1:-1}),o).bind(function(r){if(r.offset>=a.length){var t=e.createRng();return t.setStart(r.container,r.offset-a.length),t.setEnd(r.container,r.offset),at.some(t)}t=r.offset-a.length;return Et(r.container,t,o).map(function(t){var n=e.createRng();return n.setStart(t.container,t.offset),n.setEnd(r.container,r.offset),n}).filter(function(t){return t.toString()===a}).orThunk(function(){return Tt(e,n,o,S(r.container,0))})})},Nt=function(f,c,s,l,d){var m=f.dom;return _(s,l,m.getRoot()).bind(function(t){var n=m.createRng();n.setStart(d,0),n.setEnd(s,l);for(var r,e,o=n.toString(),a=0;a<c.length;a++){var i=c[a];if(r=o,e=i.end,u=void 0,u=e,e=(r=r).length-e.length,""===u||r.length>=u.length&&r.substr(e,e+u.length)===u){var u=c.slice();u.splice(a,1);u=Q(f,d,{pattern:i,remainingPatterns:u,position:t});if(u.isSome())return u}}return at.none()})};t.add("textpattern",function(t){var n,r,n=(n=function(t){t=t.getParam("textpattern_patterns",vt,"array");if(!ft(t))return N("The setting textpattern_patterns should be an array"),{inlinePatterns:[],blockPatterns:[]};t=k(m(t,E));return g(t.errors,function(t){return N(t.message,t.pattern),0}),R(t.values)}(t),r=n,{get:function(){return r},set:function(t){r=t}});return et(t,n),T(n)})}();