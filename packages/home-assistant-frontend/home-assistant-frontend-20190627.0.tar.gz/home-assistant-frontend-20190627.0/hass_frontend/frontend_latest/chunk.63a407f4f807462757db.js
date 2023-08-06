/*! For license information please see chunk.63a407f4f807462757db.js.LICENSE */
(window.webpackJsonp=window.webpackJsonp||[]).push([[35],{117:function(e,t,r){"use strict";r.d(t,"a",function(){return o});r(4);var i=r(53),n=r(34);const o=[i.a,n.a,{hostAttributes:{role:"option",tabindex:"0"}}]},136:function(e,t,r){"use strict";r(4),r(44),r(137);var i=r(5),n=r(3),o=r(117);Object(i.a)({_template:n.a`
    <style include="paper-item-shared-styles">
      :host {
        @apply --layout-horizontal;
        @apply --layout-center;
        @apply --paper-font-subhead;

        @apply --paper-item;
      }
    </style>
    <slot></slot>
`,is:"paper-item",behaviors:[o.a]})},137:function(e,t,r){"use strict";r(44),r(55),r(41),r(52);const i=document.createElement("template");i.setAttribute("style","display: none;"),i.innerHTML="<dom-module id=\"paper-item-shared-styles\">\n  <template>\n    <style>\n      :host, .paper-item {\n        display: block;\n        position: relative;\n        min-height: var(--paper-item-min-height, 48px);\n        padding: 0px 16px;\n      }\n\n      .paper-item {\n        @apply --paper-font-subhead;\n        border:none;\n        outline: none;\n        background: white;\n        width: 100%;\n        text-align: left;\n      }\n\n      :host([hidden]), .paper-item[hidden] {\n        display: none !important;\n      }\n\n      :host(.iron-selected), .paper-item.iron-selected {\n        font-weight: var(--paper-item-selected-weight, bold);\n\n        @apply --paper-item-selected;\n      }\n\n      :host([disabled]), .paper-item[disabled] {\n        color: var(--paper-item-disabled-color, var(--disabled-text-color));\n\n        @apply --paper-item-disabled;\n      }\n\n      :host(:focus), .paper-item:focus {\n        position: relative;\n        outline: 0;\n\n        @apply --paper-item-focused;\n      }\n\n      :host(:focus):before, .paper-item:focus:before {\n        @apply --layout-fit;\n\n        background: currentColor;\n        content: '';\n        opacity: var(--dark-divider-opacity);\n        pointer-events: none;\n\n        @apply --paper-item-focused-before;\n      }\n    </style>\n  </template>\n</dom-module>",document.head.appendChild(i.content)},138:function(e,t,r){"use strict";r(4),r(41);var i=r(120),n=r(5),o=r(3);Object(n.a)({_template:o.a`
    <style>
      :host {
        display: block;
        padding: 8px 0;

        background: var(--paper-listbox-background-color, var(--primary-background-color));
        color: var(--paper-listbox-color, var(--primary-text-color));

        @apply --paper-listbox;
      }
    </style>

    <slot></slot>
`,is:"paper-listbox",behaviors:[i.a],hostAttributes:{role:"listbox"}})},173:function(e,t,r){"use strict";r.d(t,"a",function(){return o});r(107);const i=customElements.get("iron-icon");let n=!1;class o extends i{constructor(...e){super(...e),this._iconsetName=void 0}listen(e,t,i){super.listen(e,t,i),n||"mdi"!==this._iconsetName||(n=!0,r.e(68).then(r.bind(null,214)))}}customElements.define("ha-icon",o)},181:function(e,t,r){"use strict";r(4),r(44),r(52),r(137);var i=r(5),n=r(3),o=r(117);Object(i.a)({_template:n.a`
    <style include="paper-item-shared-styles"></style>
    <style>
      :host {
        @apply --layout-horizontal;
        @apply --layout-center;
        @apply --paper-font-subhead;

        @apply --paper-item;
        @apply --paper-icon-item;
      }

      .content-icon {
        @apply --layout-horizontal;
        @apply --layout-center;

        width: var(--paper-item-icon-width, 56px);
        @apply --paper-item-icon;
      }
    </style>

    <div id="contentIcon" class="content-icon">
      <slot name="item-icon"></slot>
    </div>
    <slot></slot>
`,is:"paper-icon-item",behaviors:[o.a]})},215:function(e,t,r){"use strict";function i(e,t){return e&&-1!==e.config.components.indexOf(t)}r.d(t,"a",function(){return i})},723:function(e,t,r){"use strict";r.r(t);var i=r(0);r(141),r(106),r(181),r(136),r(138),r(173);function n(e){var t,r=c(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function o(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function a(e){return e.decorators&&e.decorators.length}function s(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function l(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function c(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function p(e,t,r){return(p="undefined"!=typeof Reflect&&Reflect.get?Reflect.get:function(e,t,r){var i=function(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=d(e)););return e}(e,t);if(i){var n=Object.getOwnPropertyDescriptor(i,t);return n.get?n.get.call(r):n.value}})(e,t,r||e)}function d(e){return(d=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)})(e)}const u=e=>e?e.trim().split(" ").slice(0,3).map(e=>e.substr(0,1)).join(""):"user";!function(e,t,r,i){var p=function(){var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach(function(r){t.forEach(function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)},this)},this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach(function(i){t.forEach(function(t){var n=t.placement;if(t.kind===i&&("static"===n||"prototype"===n)){var o="static"===n?e:r;this.defineClassElement(o,t)}},this)},this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],n={static:[],prototype:[],own:[]};if(e.forEach(function(e){this.addElementPlacement(e,n)},this),e.forEach(function(e){if(!a(e))return r.push(e);var t=this.decorateElement(e,n);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)},this),!t)return{elements:r,finishers:i};var o=this.decorateConstructor(r,t);return i.push.apply(i,o.finishers),o.finishers=i,o},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var p=0;p<c.length;p++)this.addElementPlacement(c[p],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[i])(n)||n);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if(Symbol.iterator in Object(e)||"[object Arguments]"===Object.prototype.toString.call(e))return Array.from(e)}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance")}()).map(function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t},this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=c(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:i,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){var t=this.toElementDescriptor(e),r=l(e,"finisher"),i=this.toElementDescriptors(e.extras);return{element:t,finisher:r,extras:i}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=l(e,"finisher"),i=this.toElementDescriptors(e.elements);return{elements:i,finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}();if(i)for(var d=0;d<i.length;d++)p=i[d](p);var u=t(function(e){p.initializeInstanceElements(e,f.elements)},r),f=p.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===l.key&&e.placement===l.placement},i=0;i<e.length;i++){var n,l=e[i];if("method"===l.kind&&(n=t.find(r)))if(s(l.descriptor)||s(n.descriptor)){if(a(l)||a(n))throw new ReferenceError("Duplicated methods ("+l.key+") can't be decorated.");n.descriptor=l.descriptor}else{if(a(l)){if(a(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+l.key+").");n.decorators=l.decorators}o(l,n)}else t.push(l)}return t}(u.d.map(n)),e);p.initializeClassElements(u.F,f.elements),p.runClassFinishers(u.F,f.finishers)}([Object(i.d)("ha-user-badge")],function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"field",decorators:[Object(i.f)()],key:"user",value:void 0},{kind:"method",key:"render",value:function(){const e=this.user,t=e?u(e.name):"?";return i.e`
      ${t}
    `}},{kind:"method",key:"updated",value:function(e){p(d(r.prototype),"updated",this).call(this,e),this.toggleAttribute("long",(this.user?u(this.user.name):"?").length>2)}},{kind:"get",static:!0,key:"styles",value:function(){return i.c`
      :host {
        display: inline-block;
        box-sizing: border-box;
        width: 40px;
        line-height: 40px;
        border-radius: 50%;
        text-align: center;
        background-color: var(--light-primary-color);
        text-decoration: none;
        color: var(--primary-text-color);
        overflow: hidden;
      }

      :host([long]) {
        font-size: 80%;
      }
    `}}]}},i.a);var f=r(215),h=r(19),m=r(116);function v(e){var t,r=w(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function y(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function b(e){return e.decorators&&e.decorators.length}function g(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function x(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function w(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function k(e,t,r){return(k="undefined"!=typeof Reflect&&Reflect.get?Reflect.get:function(e,t,r){var i=function(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=E(e)););return e}(e,t);if(i){var n=Object.getOwnPropertyDescriptor(i,t);return n.get?n.get.call(r):n.value}})(e,t,r||e)}function E(e){return(E=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)})(e)}const P=e=>`/${e}`,z=(e,t)=>i.e`
  <a
    aria-role="option"
    href="${P(t.url_path)}"
    data-panel="${t.url_path}"
    tabindex="-1"
  >
    <paper-icon-item>
      <ha-icon slot="item-icon" .icon="${t.icon}"></ha-icon>
      <span class="item-text">
        ${e.localize(`panel.${t.title}`)||t.title}
      </span>
    </paper-icon-item>
  </a>
`;let O=function(e,t,r,i){var n=function(){var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach(function(r){t.forEach(function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)},this)},this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach(function(i){t.forEach(function(t){var n=t.placement;if(t.kind===i&&("static"===n||"prototype"===n)){var o="static"===n?e:r;this.defineClassElement(o,t)}},this)},this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],n={static:[],prototype:[],own:[]};if(e.forEach(function(e){this.addElementPlacement(e,n)},this),e.forEach(function(e){if(!b(e))return r.push(e);var t=this.decorateElement(e,n);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)},this),!t)return{elements:r,finishers:i};var o=this.decorateConstructor(r,t);return i.push.apply(i,o.finishers),o.finishers=i,o},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],n=e.decorators,o=n.length-1;o>=0;o--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,n[o])(s)||s);e=l.element,this.addElementPlacement(e,t),l.finisher&&i.push(l.finisher);var c=l.extras;if(c){for(var p=0;p<c.length;p++)this.addElementPlacement(c[p],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var n=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[i])(n)||n);if(void 0!==o.finisher&&r.push(o.finisher),void 0!==o.elements){e=o.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if(Symbol.iterator in Object(e)||"[object Arguments]"===Object.prototype.toString.call(e))return Array.from(e)}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance")}()).map(function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t},this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=w(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var n=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:r,placement:i,descriptor:Object.assign({},n)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){var t=this.toElementDescriptor(e),r=x(e,"finisher"),i=this.toElementDescriptors(e.extras);return{element:t,finisher:r,extras:i}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=x(e,"finisher"),i=this.toElementDescriptors(e.elements);return{elements:i,finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}();if(i)for(var o=0;o<i.length;o++)n=i[o](n);var a=t(function(e){n.initializeInstanceElements(e,s.elements)},r),s=n.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},i=0;i<e.length;i++){var n,o=e[i];if("method"===o.kind&&(n=t.find(r)))if(g(o.descriptor)||g(n.descriptor)){if(b(o)||b(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(b(o)){if(b(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}y(o,n)}else t.push(o)}return t}(a.d.map(v)),e);return n.initializeClassElements(a.F,s.elements),n.runClassFinishers(a.F,s.finishers)}(null,function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"field",decorators:[Object(i.f)()],key:"hass",value:void 0},{kind:"field",decorators:[Object(i.f)({type:Boolean})],key:"alwaysExpand",value:()=>!1},{kind:"field",decorators:[Object(i.f)({type:Boolean,reflect:!0})],key:"expanded",value:()=>!1},{kind:"field",decorators:[Object(i.f)()],key:"_defaultPage",value:()=>localStorage.defaultPage||m.b},{kind:"field",decorators:[Object(i.f)()],key:"_externalConfig",value:void 0},{kind:"method",key:"render",value:function(){const e=this.hass;if(!e)return i.e``;const t=(e=>{const t=e.panels;if(!t)return[];const r={map:1,logbook:2,history:3},i=Object.values(t).filter(e=>e.title);return i.sort((e,t)=>{const i=e.component_name in r,n=t.component_name in r;return i&&n?r[e.component_name]-r[t.component_name]:i?-1:n?1:e.title<t.title?-1:e.title>t.title?1:0}),i})(e),r=t.findIndex(e=>"config"===e.component_name),n=-1===r?void 0:t.splice(r,1)[0];return i.e`
      ${this.expanded?i.e`
            <app-toolbar>
              <div main-title>Home Assistant</div>
            </app-toolbar>
          `:i.e`
            <div class="logo">
              <img
                id="logo"
                src="/static/icons/favicon-192x192.png"
                alt="Home Assistant logo"
              />
            </div>
          `}

      <paper-listbox attr-for-selected="data-panel" .selected=${e.panelUrl}>
        <a
          aria-role="option"
          href="${P(this._defaultPage)}"
          data-panel=${this._defaultPage}
          tabindex="-1"
        >
          <paper-icon-item>
            <ha-icon slot="item-icon" icon="hass:apps"></ha-icon>
            <span class="item-text">${e.localize("panel.states")}</span>
          </paper-icon-item>
        </a>

        ${t.map(t=>z(e,t))}

        <div class="spacer" disabled></div>

        ${this.expanded&&e.user&&e.user.is_admin?i.e`
              <div class="divider" disabled></div>

              <div class="subheader" disabled>
                ${e.localize("ui.sidebar.developer_tools")}
              </div>

              <div class="dev-tools" disabled>
                <a href="/dev-service" tabindex="-1">
                  <paper-icon-button
                    icon="hass:remote"
                    alt="${e.localize("panel.dev-services")}"
                    title="${e.localize("panel.dev-services")}"
                  ></paper-icon-button>
                </a>
                <a href="/dev-state" tabindex="-1">
                  <paper-icon-button
                    icon="hass:code-tags"
                    alt="${e.localize("panel.dev-states")}"
                    title="${e.localize("panel.dev-states")}"
                  ></paper-icon-button>
                </a>
                <a href="/dev-event" tabindex="-1">
                  <paper-icon-button
                    icon="hass:radio-tower"
                    alt="${e.localize("panel.dev-events")}"
                    title="${e.localize("panel.dev-events")}"
                  ></paper-icon-button>
                </a>
                <a href="/dev-template" tabindex="-1">
                  <paper-icon-button
                    icon="hass:file-xml"
                    alt="${e.localize("panel.dev-templates")}"
                    title="${e.localize("panel.dev-templates")}"
                  ></paper-icon-button>
                </a>
                ${Object(f.a)(e,"mqtt")?i.e`
                      <a href="/dev-mqtt" tabindex="-1">
                        <paper-icon-button
                          icon="hass:altimeter"
                          alt="${e.localize("panel.dev-mqtt")}"
                          title="${e.localize("panel.dev-mqtt")}"
                        ></paper-icon-button>
                      </a>
                    `:i.e``}
                <a href="/dev-info" tabindex="-1">
                  <paper-icon-button
                    icon="hass:information-outline"
                    alt="${e.localize("panel.dev-info")}"
                    title="${e.localize("panel.dev-info")}"
                  ></paper-icon-button>
                </a>
              </div>
              <div class="divider" disabled></div>
            `:""}
        ${this._externalConfig&&this._externalConfig.hasSettingsScreen?i.e`
              <a
                aria-role="option"
                aria-label="App Configuration"
                href="#external-app-configuration"
                tabindex="-1"
                @click=${this._handleExternalAppConfiguration}
              >
                <paper-icon-item>
                  <ha-icon
                    slot="item-icon"
                    icon="hass:cellphone-settings-variant"
                  ></ha-icon>
                  <span class="item-text"
                    >${e.localize("ui.sidebar.external_app_configuration")}</span
                  >
                </paper-icon-item>
              </a>
            `:""}
        ${n?z(e,n):""}
        ${e.user?i.e`
              <a
                href="/profile"
                data-panel="panel"
                tabindex="-1"
                aria-role="option"
                aria-label=${e.localize("panel.profile")}
              >
                <paper-icon-item class="profile">
                  <ha-user-badge
                    slot="item-icon"
                    .user=${e.user}
                  ></ha-user-badge>

                  <span class="item-text">
                    ${e.user.name}
                  </span>
                </paper-icon-item>
              </a>
            `:i.e`
              <paper-icon-item
                @click=${this._handleLogOut}
                class="logout"
                aria-role="option"
              >
                <ha-icon slot="item-icon" icon="hass:exit-to-app"></ha-icon>
                <span class="item-text"
                  >${e.localize("ui.sidebar.log_out")}</span
                >
              </paper-icon-item>
            `}
      </paper-listbox>
    `}},{kind:"method",key:"shouldUpdate",value:function(e){if(e.has("_externalConfig")||e.has("expanded")||e.has("alwaysExpand"))return!0;if(!this.hass||!e.has("hass"))return!1;const t=e.get("hass");if(!t)return!0;const r=this.hass;return r.panels!==t.panels||r.panelUrl!==t.panelUrl||r.config.components!==t.config.components||r.user!==t.user||r.localize!==t.localize}},{kind:"method",key:"firstUpdated",value:function(e){k(E(r.prototype),"firstUpdated",this).call(this,e),this.hass&&this.hass.auth.external&&(e=>(e.cache.cfg||(e.cache.cfg=e.sendMessage({type:"config/get"})),e.cache.cfg))(this.hass.auth.external).then(e=>{this._externalConfig=e}),this.shadowRoot.querySelector("paper-listbox").addEventListener("mouseenter",()=>{this.expanded=!0}),this.addEventListener("mouseleave",()=>{this._contract()})}},{kind:"method",key:"updated",value:function(e){k(E(r.prototype),"updated",this).call(this,e),e.has("alwaysExpand")&&(this.expanded=this.alwaysExpand)}},{kind:"method",key:"_contract",value:function(){this.expanded=this.alwaysExpand||!1}},{kind:"method",key:"_handleLogOut",value:function(){Object(h.a)(this,"hass-logout")}},{kind:"method",key:"_handleExternalAppConfiguration",value:function(e){e.preventDefault(),this.hass.auth.external.fireMessage({type:"config_screen/show"})}},{kind:"get",static:!0,key:"styles",value:function(){return i.c`
      :host {
        height: 100%;
        display: block;
        overflow: hidden auto;
        -ms-user-select: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        border-right: 1px solid var(--divider-color);
        background-color: var(
          --sidebar-background-color,
          var(--primary-background-color)
        );
        width: 64px;
        transition: width 0.2s ease-in;
        will-change: width;
        contain: strict;
      }
      :host([expanded]) {
        width: 256px;
      }

      .logo {
        height: 65px;
        box-sizing: border-box;
        padding: 8px;
        border-bottom: 1px solid transparent;
      }
      .logo img {
        width: 48px;
      }

      app-toolbar {
        white-space: nowrap;
        font-weight: 400;
        color: var(--primary-text-color);
        border-bottom: 1px solid var(--divider-color);
        background-color: var(--primary-background-color);
      }

      app-toolbar a {
        color: var(--primary-text-color);
      }

      paper-listbox {
        padding: 4px 0;
        height: calc(100% - 65px);
        display: flex;
        flex-direction: column;
        box-sizing: border-box;
      }

      paper-listbox > a {
        color: var(--sidebar-text-color);
        font-weight: 500;
        font-size: 14px;
        text-decoration: none;
      }

      paper-icon-item {
        box-sizing: border-box;
        margin: 4px 8px;
        padding-left: 12px;
        border-radius: 4px;
        --paper-item-min-height: 40px;
        width: 48px;
      }
      :host([expanded]) paper-icon-item {
        width: 240px;
      }

      ha-icon[slot="item-icon"] {
        color: var(--sidebar-icon-color);
      }

      .iron-selected paper-icon-item:before {
        border-radius: 4px;
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        pointer-events: none;
        content: "";
        background-color: var(--sidebar-selected-icon-color);
        opacity: 0.12;
        transition: opacity 15ms linear;
        will-change: opacity;
      }

      .iron-selected paper-icon-item[pressed]:before {
        opacity: 0.37;
      }

      paper-icon-item span {
        color: var(--sidebar-text-color);
        font-weight: 500;
        font-size: 14px;
      }

      a.iron-selected paper-icon-item ha-icon {
        color: var(--sidebar-selected-icon-color);
      }

      a.iron-selected .item-text {
        color: var(--sidebar-selected-text-color);
      }

      a .item-text {
        display: none;
      }
      :host([expanded]) a .item-text {
        display: block;
      }

      paper-icon-item.logout {
        margin-top: 16px;
      }

      paper-icon-item.profile {
        padding-left: 4px;
      }
      .profile .item-text {
        margin-left: 8px;
      }

      .spacer {
        flex: 1;
        pointer-events: none;
      }

      .divider {
        height: 1px;
        background-color: var(--divider-color);
        margin: 4px 0;
      }

      .subheader {
        color: var(--sidebar-text-color);
        font-weight: 500;
        font-size: 14px;
        padding: 16px;
        white-space: nowrap;
      }

      .dev-tools {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        padding: 0 8px;
        width: 256px;
        box-sizing: border-box;
      }

      .dev-tools a {
        color: var(--sidebar-icon-color);
      }
    `}}]}},i.a);customElements.define("ha-sidebar",O)}}]);
//# sourceMappingURL=chunk.63a407f4f807462757db.js.map