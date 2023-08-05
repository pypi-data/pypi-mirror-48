/*! For license information please see chunk.471708b543d0bbc92b18.js.LICENSE */
(window.webpackJsonp=window.webpackJsonp||[]).push([[29],{118:function(n,e,t){"use strict";t(5);var i={properties:{animationConfig:{type:Object},entryAnimation:{observer:"_entryAnimationChanged",type:String},exitAnimation:{observer:"_exitAnimationChanged",type:String}},_entryAnimationChanged:function(){this.animationConfig=this.animationConfig||{},this.animationConfig.entry=[{name:this.entryAnimation,node:this}]},_exitAnimationChanged:function(){this.animationConfig=this.animationConfig||{},this.animationConfig.exit=[{name:this.exitAnimation,node:this}]},_copyProperties:function(n,e){for(var t in e)n[t]=e[t]},_cloneConfig:function(n){var e={isClone:!0};return this._copyProperties(e,n),e},_getAnimationConfigRecursive:function(n,e,t){var i;if(this.animationConfig)if(this.animationConfig.value&&"function"==typeof this.animationConfig.value)this._warn(this._logf("playAnimation","Please put 'animationConfig' inside of your components 'properties' object instead of outside of it."));else if(i=n?this.animationConfig[n]:this.animationConfig,Array.isArray(i)||(i=[i]),i)for(var o,a=0;o=i[a];a++)if(o.animatable)o.animatable._getAnimationConfigRecursive(o.type||n,e,t);else if(o.id){var r=e[o.id];r?(r.isClone||(e[o.id]=this._cloneConfig(r),r=e[o.id]),this._copyProperties(r,o)):e[o.id]=o}else t.push(o)},getAnimationConfig:function(n){var e={},t=[];for(var i in this._getAnimationConfigRecursive(n,e,t),e)t.push(e[i]);return t}};t.d(e,"a",function(){return o});var o=[i,{_configureAnimations:function(n){var e=[],t=[];if(n.length>0)for(var i,o=0;i=n[o];o++){var a=document.createElement(i.name);if(a.isNeonAnimation){var r;a.configure||(a.configure=function(n){return null}),r=a.configure(i),t.push({result:r,config:i,neonAnimation:a})}else console.warn(this.is+":",i.name,"not found!")}for(var s=0;s<t.length;s++){var l=t[s].result,c=t[s].config,p=t[s].neonAnimation;try{"function"!=typeof l.cancel&&(l=document.timeline.play(l))}catch(d){l=null,console.warn("Couldnt play","(",c.name,").",d)}l&&e.push({neonAnimation:p,config:c,animation:l})}return e},_shouldComplete:function(n){for(var e=!0,t=0;t<n.length;t++)if("finished"!=n[t].animation.playState){e=!1;break}return e},_complete:function(n){for(var e=0;e<n.length;e++)n[e].neonAnimation.complete(n[e].config);for(e=0;e<n.length;e++)n[e].animation.cancel()},playAnimation:function(n,e){var t=this.getAnimationConfig(n);if(t){this._active=this._active||{},this._active[n]&&(this._complete(this._active[n]),delete this._active[n]);var i=this._configureAnimations(t);if(0!=i.length){this._active[n]=i;for(var o=0;o<i.length;o++)i[o].animation.onfinish=function(){this._shouldComplete(i)&&(this._complete(i),delete this._active[n],this.fire("neon-animation-finish",e,{bubbles:!1}))}.bind(this)}else this.fire("neon-animation-finish",e,{bubbles:!1})}},cancelAnimation:function(){for(var n in this._active){var e=this._active[n];for(var t in e)e[t].animation.cancel()}this._active={}}}]},178:function(n,e,t){"use strict";t.d(e,"b",function(){return a}),t.d(e,"a",function(){return r});t(5);var i=t(84),o=t(2),a={hostAttributes:{role:"dialog",tabindex:"-1"},properties:{modal:{type:Boolean,value:!1},__readied:{type:Boolean,value:!1}},observers:["_modalChanged(modal, __readied)"],listeners:{tap:"_onDialogClick"},ready:function(){this.__prevNoCancelOnOutsideClick=this.noCancelOnOutsideClick,this.__prevNoCancelOnEscKey=this.noCancelOnEscKey,this.__prevWithBackdrop=this.withBackdrop,this.__readied=!0},_modalChanged:function(n,e){e&&(n?(this.__prevNoCancelOnOutsideClick=this.noCancelOnOutsideClick,this.__prevNoCancelOnEscKey=this.noCancelOnEscKey,this.__prevWithBackdrop=this.withBackdrop,this.noCancelOnOutsideClick=!0,this.noCancelOnEscKey=!0,this.withBackdrop=!0):(this.noCancelOnOutsideClick=this.noCancelOnOutsideClick&&this.__prevNoCancelOnOutsideClick,this.noCancelOnEscKey=this.noCancelOnEscKey&&this.__prevNoCancelOnEscKey,this.withBackdrop=this.withBackdrop&&this.__prevWithBackdrop))},_updateClosingReasonConfirmed:function(n){this.closingReason=this.closingReason||{},this.closingReason.confirmed=n},_onDialogClick:function(n){for(var e=Object(o.a)(n).path,t=0,i=e.indexOf(this);t<i;t++){var a=e[t];if(a.hasAttribute&&(a.hasAttribute("dialog-dismiss")||a.hasAttribute("dialog-confirm"))){this._updateClosingReasonConfirmed(a.hasAttribute("dialog-confirm")),this.close(),n.stopPropagation();break}}}},r=[i.a,a]},179:function(n,e,t){"use strict";t(5),t(56),t(144);var i=t(6),o=t(4),a=t(122);function r(){var n=function(n,e){e||(e=n.slice(0));return Object.freeze(Object.defineProperties(n,{raw:{value:Object.freeze(e)}}))}(['\n  <style include="paper-spinner-styles"></style>\n\n  <div id="spinnerContainer" class-name="[[__computeContainerClasses(active, __coolingDown)]]" on-animationend="__reset" on-webkit-animation-end="__reset">\n    <div class="spinner-layer layer-1">\n      <div class="circle-clipper left">\n        <div class="circle"></div>\n      </div>\n      <div class="circle-clipper right">\n        <div class="circle"></div>\n      </div>\n    </div>\n\n    <div class="spinner-layer layer-2">\n      <div class="circle-clipper left">\n        <div class="circle"></div>\n      </div>\n      <div class="circle-clipper right">\n        <div class="circle"></div>\n      </div>\n    </div>\n\n    <div class="spinner-layer layer-3">\n      <div class="circle-clipper left">\n        <div class="circle"></div>\n      </div>\n      <div class="circle-clipper right">\n        <div class="circle"></div>\n      </div>\n    </div>\n\n    <div class="spinner-layer layer-4">\n      <div class="circle-clipper left">\n        <div class="circle"></div>\n      </div>\n      <div class="circle-clipper right">\n        <div class="circle"></div>\n      </div>\n    </div>\n  </div>\n']);return r=function(){return n},n}var s=Object(o.a)(r());s.setAttribute("strip-whitespace",""),Object(i.a)({_template:s,is:"paper-spinner",behaviors:[a.a]})},183:function(n,e,t){"use strict";t(5),t(46),t(44),t(53),t(83);var i=document.createElement("template");i.setAttribute("style","display: none;"),i.innerHTML='<dom-module id="paper-dialog-shared-styles">\n  <template>\n    <style>\n      :host {\n        display: block;\n        margin: 24px 40px;\n\n        background: var(--paper-dialog-background-color, var(--primary-background-color));\n        color: var(--paper-dialog-color, var(--primary-text-color));\n\n        @apply --paper-font-body1;\n        @apply --shadow-elevation-16dp;\n        @apply --paper-dialog;\n      }\n\n      :host > ::slotted(*) {\n        margin-top: 20px;\n        padding: 0 24px;\n      }\n\n      :host > ::slotted(.no-padding) {\n        padding: 0;\n      }\n\n      \n      :host > ::slotted(*:first-child) {\n        margin-top: 24px;\n      }\n\n      :host > ::slotted(*:last-child) {\n        margin-bottom: 24px;\n      }\n\n      /* In 1.x, this selector was `:host > ::content h2`. In 2.x <slot> allows\n      to select direct children only, which increases the weight of this\n      selector, so we have to re-define first-child/last-child margins below. */\n      :host > ::slotted(h2) {\n        position: relative;\n        margin: 0;\n\n        @apply --paper-font-title;\n        @apply --paper-dialog-title;\n      }\n\n      /* Apply mixin again, in case it sets margin-top. */\n      :host > ::slotted(h2:first-child) {\n        margin-top: 24px;\n        @apply --paper-dialog-title;\n      }\n\n      /* Apply mixin again, in case it sets margin-bottom. */\n      :host > ::slotted(h2:last-child) {\n        margin-bottom: 24px;\n        @apply --paper-dialog-title;\n      }\n\n      :host > ::slotted(.paper-dialog-buttons),\n      :host > ::slotted(.buttons) {\n        position: relative;\n        padding: 8px 8px 8px 24px;\n        margin: 0;\n\n        color: var(--paper-dialog-button-color, var(--primary-color));\n\n        @apply --layout-horizontal;\n        @apply --layout-end-justified;\n      }\n    </style>\n  </template>\n</dom-module>',document.head.appendChild(i.content)},187:function(n,e,t){"use strict";t(5),t(183);var i=t(118),o=t(178),a=t(6),r=t(4);function s(){var n=function(n,e){e||(e=n.slice(0));return Object.freeze(Object.defineProperties(n,{raw:{value:Object.freeze(e)}}))}(['\n    <style include="paper-dialog-shared-styles"></style>\n    <slot></slot>\n']);return s=function(){return n},n}Object(a.a)({_template:Object(r.a)(s()),is:"paper-dialog",behaviors:[o.a,i.a],listeners:{"neon-animation-finish":"_onNeonAnimationFinish"},_renderOpened:function(){this.cancelAnimation(),this.playAnimation("entry")},_renderClosed:function(){this.cancelAnimation(),this.playAnimation("exit")},_onNeonAnimationFinish:function(){this.opened?this._finishRenderOpened():this._finishRenderClosed()}})},189:function(n,e,t){"use strict";t(187);var i=t(70),o=t(2),a=t(123),r={getTabbableNodes:function(n){var e=[];return this._collectTabbableNodes(n,e)?a.a._sortByTabIndex(e):e},_collectTabbableNodes:function(n,e){if(n.nodeType!==Node.ELEMENT_NODE||!a.a._isVisible(n))return!1;var t,i=n,r=a.a._normalizedTabIndex(i),s=r>0;r>=0&&e.push(i),t="content"===i.localName||"slot"===i.localName?Object(o.a)(i).getDistributedNodes():Object(o.a)(i.shadowRoot||i.root||i).children;for(var l=0;l<t.length;l++)s=this._collectTabbableNodes(t[l],e)||s;return s}};function s(n){return(s="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(n){return typeof n}:function(n){return n&&"function"==typeof Symbol&&n.constructor===Symbol&&n!==Symbol.prototype?"symbol":typeof n})(n)}function l(n,e){return!e||"object"!==s(e)&&"function"!=typeof e?function(n){if(void 0===n)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return n}(n):e}function c(n){return(c=Object.setPrototypeOf?Object.getPrototypeOf:function(n){return n.__proto__||Object.getPrototypeOf(n)})(n)}function p(n,e){return(p=Object.setPrototypeOf||function(n,e){return n.__proto__=e,n})(n,e)}var d=customElements.get("paper-dialog"),u={get _focusableNodes(){return r.getTabbableNodes(this)}},h=function(n){function e(){return function(n,e){if(!(n instanceof e))throw new TypeError("Cannot call a class as a function")}(this,e),l(this,c(e).apply(this,arguments))}return function(n,e){if("function"!=typeof e&&null!==e)throw new TypeError("Super expression must either be null or a function");n.prototype=Object.create(e&&e.prototype,{constructor:{value:n,writable:!0,configurable:!0}}),e&&p(n,e)}(e,Object(i["b"])([u],d)),e}();customElements.define("ha-paper-dialog",h)},650:function(n,e,t){"use strict";t.r(e);t(82),t(179);var i=t(4),o=t(26),a=(t(92),t(189),t(168));function r(n){return(r="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(n){return typeof n}:function(n){return n&&"function"==typeof Symbol&&n.constructor===Symbol&&n!==Symbol.prototype?"symbol":typeof n})(n)}function s(){var n=function(n,e){e||(e=n.slice(0));return Object.freeze(Object.defineProperties(n,{raw:{value:Object.freeze(e)}}))}(['\n      <style include="ha-style-dialog">\n        .error {\n          color: red;\n        }\n        @media all and (max-width: 500px) {\n          ha-paper-dialog {\n            margin: 0;\n            width: 100%;\n            max-height: calc(100% - 64px);\n\n            position: fixed !important;\n            bottom: 0px;\n            left: 0px;\n            right: 0px;\n            overflow: scroll;\n            border-bottom-left-radius: 0px;\n            border-bottom-right-radius: 0px;\n          }\n        }\n\n        ha-paper-dialog {\n          border-radius: 2px;\n        }\n        ha-paper-dialog p {\n          color: var(--secondary-text-color);\n        }\n\n        .icon {\n          float: right;\n        }\n      </style>\n      <ha-paper-dialog\n        id="mp3dialog"\n        with-backdrop\n        opened="{{_opened}}"\n        on-opened-changed="_openedChanged"\n      >\n        <h2>\n          [[localize(\'ui.panel.mailbox.playback_title\')]]\n          <div class="icon">\n            <template is="dom-if" if="[[_loading]]">\n              <paper-spinner active></paper-spinner>\n            </template>\n            <paper-icon-button\n              id="delicon"\n              on-click="openDeleteDialog"\n              icon="hass:delete"\n            ></paper-icon-button>\n          </div>\n        </h2>\n        <div id="transcribe"></div>\n        <div>\n          <template is="dom-if" if="[[_errorMsg]]">\n            <div class="error">[[_errorMsg]]</div>\n          </template>\n          <audio id="mp3" preload="none" controls>\n            <source id="mp3src" src="" type="audio/mpeg" />\n          </audio>\n        </div>\n      </ha-paper-dialog>\n    ']);return s=function(){return n},n}function l(n,e){for(var t=0;t<e.length;t++){var i=e[t];i.enumerable=i.enumerable||!1,i.configurable=!0,"value"in i&&(i.writable=!0),Object.defineProperty(n,i.key,i)}}function c(n,e){return!e||"object"!==r(e)&&"function"!=typeof e?function(n){if(void 0===n)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return n}(n):e}function p(n){return(p=Object.setPrototypeOf?Object.getPrototypeOf:function(n){return n.__proto__||Object.getPrototypeOf(n)})(n)}function d(n,e){return(d=Object.setPrototypeOf||function(n,e){return n.__proto__=e,n})(n,e)}var u=function(n){function e(){return function(n,e){if(!(n instanceof e))throw new TypeError("Cannot call a class as a function")}(this,e),c(this,p(e).apply(this,arguments))}var t,r,u;return function(n,e){if("function"!=typeof e&&null!==e)throw new TypeError("Super expression must either be null or a function");n.prototype=Object.create(e&&e.prototype,{constructor:{value:n,writable:!0,configurable:!0}}),e&&d(n,e)}(e,Object(a["a"])(o["a"])),t=e,u=[{key:"template",get:function(){return Object(i.a)(s())}},{key:"properties",get:function(){return{hass:Object,_currentMessage:Object,_errorMsg:String,_loading:{type:Boolean,value:!1},_opened:{type:Boolean,value:!1}}}}],(r=[{key:"showDialog",value:function(n){var e=this,t=n.hass,i=n.message;this.hass=t,this._errorMsg=null,this._currentMessage=i,this._opened=!0,this.$.transcribe.innerText=i.message;var o=i.platform,a=this.$.mp3;if(o.has_media){a.style.display="",this._showLoading(!0),a.src=null;var r="/api/mailbox/media/".concat(o.name,"/").concat(i.sha);this.hass.fetchWithAuth(r).then(function(n){return n.ok?n.blob():Promise.reject({status:n.status,statusText:n.statusText})}).then(function(n){e._showLoading(!1),a.src=window.URL.createObjectURL(n),a.play()}).catch(function(n){e._showLoading(!1),e._errorMsg="Error loading audio: ".concat(n.statusText)})}else a.style.display="none",this._showLoading(!1)}},{key:"openDeleteDialog",value:function(){confirm(this.localize("ui.panel.mailbox.delete_prompt"))&&this.deleteSelected()}},{key:"deleteSelected",value:function(){var n=this._currentMessage;this.hass.callApi("DELETE","mailbox/delete/".concat(n.platform.name,"/").concat(n.sha)),this._dialogDone()}},{key:"_dialogDone",value:function(){this.$.mp3.pause(),this.setProperties({_currentMessage:null,_errorMsg:null,_loading:!1,_opened:!1})}},{key:"_openedChanged",value:function(n){n.detail.value||this._dialogDone()}},{key:"_showLoading",value:function(n){var e=this.$.delicon;if(n)this._loading=!0,e.style.display="none";else{var t=this._currentMessage.platform;this._loading=!1,e.style.display=t.can_delete?"":"none"}}}])&&l(t.prototype,r),u&&l(t,u),e}();customElements.define("ha-dialog-show-audio-message",u)}}]);
//# sourceMappingURL=chunk.471708b543d0bbc92b18.js.map