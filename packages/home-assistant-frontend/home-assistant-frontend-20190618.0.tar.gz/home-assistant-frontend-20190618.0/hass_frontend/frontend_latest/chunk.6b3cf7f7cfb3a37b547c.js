/*! For license information please see chunk.6b3cf7f7cfb3a37b547c.js.LICENSE */
(window.webpackJsonp=window.webpackJsonp||[]).push([[98],{105:function(t,e,i){"use strict";i.d(e,"a",function(){return n});var a=i(10),s=i(21);const n=Object(a.a)(t=>(class extends t{fire(t,e,i){return i=i||{},Object(s.a)(i.node||this,t,e,i)}}))},167:function(t,e,i){"use strict";var a=i(10);e.a=Object(a.a)(t=>(class extends t{static get properties(){return{hass:Object,localize:{type:Function,computed:"__computeLocalize(hass.localize)"}}}__computeLocalize(t){return t}}))},169:function(t,e,i){"use strict";var a=i(185);e.a=(t=>void 0===t.attributes.friendly_name?Object(a.a)(t.entity_id).replace(/_/g," "):t.attributes.friendly_name||"")},171:function(t,e,i){"use strict";i.d(e,"a",function(){return s});var a=i(174);function s(t){return Object(a.a)(t.entity_id)}},173:function(t,e,i){"use strict";i.d(e,"a",function(){return n});i(107);const a=customElements.get("iron-icon");let s=!1;class n extends a{constructor(...t){super(...t),this._iconsetName=void 0}listen(t,e,a){super.listen(t,e,a),s||"mdi"!==this._iconsetName||(s=!0,i.e(64).then(i.bind(null,214)))}}customElements.define("ha-icon",n)},174:function(t,e,i){"use strict";function a(t){return t.substr(0,t.indexOf("."))}i.d(e,"a",function(){return a})},185:function(t,e,i){"use strict";function a(t){return t.substr(t.indexOf(".")+1)}i.d(e,"a",function(){return a})},243:function(t,e,i){"use strict";i(5);var a=i(6),s=i(4),n=i(20);Object(a.a)({_template:s.a`
    <style>
      :host {
        display: inline-block;
        overflow: hidden;
        position: relative;
      }

      #baseURIAnchor {
        display: none;
      }

      #sizedImgDiv {
        position: absolute;
        top: 0px;
        right: 0px;
        bottom: 0px;
        left: 0px;

        display: none;
      }

      #img {
        display: block;
        width: var(--iron-image-width, auto);
        height: var(--iron-image-height, auto);
      }

      :host([sizing]) #sizedImgDiv {
        display: block;
      }

      :host([sizing]) #img {
        display: none;
      }

      #placeholder {
        position: absolute;
        top: 0px;
        right: 0px;
        bottom: 0px;
        left: 0px;

        background-color: inherit;
        opacity: 1;

        @apply --iron-image-placeholder;
      }

      #placeholder.faded-out {
        transition: opacity 0.5s linear;
        opacity: 0;
      }
    </style>

    <a id="baseURIAnchor" href="#"></a>
    <div id="sizedImgDiv" role="img" hidden$="[[_computeImgDivHidden(sizing)]]" aria-hidden$="[[_computeImgDivARIAHidden(alt)]]" aria-label$="[[_computeImgDivARIALabel(alt, src)]]"></div>
    <img id="img" alt$="[[alt]]" hidden$="[[_computeImgHidden(sizing)]]" crossorigin$="[[crossorigin]]" on-load="_imgOnLoad" on-error="_imgOnError">
    <div id="placeholder" hidden$="[[_computePlaceholderHidden(preload, fade, loading, loaded)]]" class$="[[_computePlaceholderClassName(preload, fade, loading, loaded)]]"></div>
`,is:"iron-image",properties:{src:{type:String,value:""},alt:{type:String,value:null},crossorigin:{type:String,value:null},preventLoad:{type:Boolean,value:!1},sizing:{type:String,value:null,reflectToAttribute:!0},position:{type:String,value:"center"},preload:{type:Boolean,value:!1},placeholder:{type:String,value:null,observer:"_placeholderChanged"},fade:{type:Boolean,value:!1},loaded:{notify:!0,readOnly:!0,type:Boolean,value:!1},loading:{notify:!0,readOnly:!0,type:Boolean,value:!1},error:{notify:!0,readOnly:!0,type:Boolean,value:!1},width:{observer:"_widthChanged",type:Number,value:null},height:{observer:"_heightChanged",type:Number,value:null}},observers:["_transformChanged(sizing, position)","_loadStateObserver(src, preventLoad)"],created:function(){this._resolvedSrc=""},_imgOnLoad:function(){this.$.img.src===this._resolveSrc(this.src)&&(this._setLoading(!1),this._setLoaded(!0),this._setError(!1))},_imgOnError:function(){this.$.img.src===this._resolveSrc(this.src)&&(this.$.img.removeAttribute("src"),this.$.sizedImgDiv.style.backgroundImage="",this._setLoading(!1),this._setLoaded(!1),this._setError(!0))},_computePlaceholderHidden:function(){return!this.preload||!this.fade&&!this.loading&&this.loaded},_computePlaceholderClassName:function(){return this.preload&&this.fade&&!this.loading&&this.loaded?"faded-out":""},_computeImgDivHidden:function(){return!this.sizing},_computeImgDivARIAHidden:function(){return""===this.alt?"true":void 0},_computeImgDivARIALabel:function(){return null!==this.alt?this.alt:""===this.src?"":this._resolveSrc(this.src).replace(/[?|#].*/g,"").split("/").pop()},_computeImgHidden:function(){return!!this.sizing},_widthChanged:function(){this.style.width=isNaN(this.width)?this.width:this.width+"px"},_heightChanged:function(){this.style.height=isNaN(this.height)?this.height:this.height+"px"},_loadStateObserver:function(t,e){var i=this._resolveSrc(t);i!==this._resolvedSrc&&(this._resolvedSrc="",this.$.img.removeAttribute("src"),this.$.sizedImgDiv.style.backgroundImage="",""===t||e?(this._setLoading(!1),this._setLoaded(!1),this._setError(!1)):(this._resolvedSrc=i,this.$.img.src=this._resolvedSrc,this.$.sizedImgDiv.style.backgroundImage='url("'+this._resolvedSrc+'")',this._setLoading(!0),this._setLoaded(!1),this._setError(!1)))},_placeholderChanged:function(){this.$.placeholder.style.backgroundImage=this.placeholder?'url("'+this.placeholder+'")':""},_transformChanged:function(){var t=this.$.sizedImgDiv.style,e=this.$.placeholder.style;t.backgroundSize=e.backgroundSize=this.sizing,t.backgroundPosition=e.backgroundPosition=this.sizing?this.position:"",t.backgroundRepeat=e.backgroundRepeat=this.sizing?"no-repeat":""},_resolveSrc:function(t){var e=Object(n.c)(t,this.$.baseURIAnchor.href);return e.length>=2&&"/"===e[0]&&"/"!==e[1]&&(e=(location.origin||location.protocol+"//"+location.host)+e),e}})},280:function(t,e,i){"use strict";i.d(e,"a",function(){return a});const a=async(t,e=!1)=>{if(!t.parentNode)throw new Error("Cannot setup Leaflet map on disconnected element");const a=await i.e(122).then(i.t.bind(null,352,7));a.Icon.Default.imagePath="/static/images/leaflet/images/";const s=a.map(t),n=document.createElement("link");return n.setAttribute("href","/static/images/leaflet/leaflet.css"),n.setAttribute("rel","stylesheet"),t.parentNode.appendChild(n),s.setView([52.3731339,4.8903147],13),a.tileLayer(`https://{s}.basemaps.cartocdn.com/${e?"dark_all":"light_all"}/{z}/{x}/{y}${a.Browser.retina?"@2x.png":".png"}`,{attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attributions">CARTO</a>',subdomains:"abcd",minZoom:0,maxZoom:20}).addTo(s),[s,a]}},387:function(t,e,i){"use strict";i(243);var a=i(4),s=i(26),n=i(105);customElements.define("ha-entity-marker",class extends(Object(n.a)(s.a)){static get template(){return a.a`
      <style include="iron-positioning"></style>
      <style>
        .marker {
          vertical-align: top;
          position: relative;
          display: block;
          margin: 0 auto;
          width: 2.5em;
          text-align: center;
          height: 2.5em;
          line-height: 2.5em;
          font-size: 1.5em;
          border-radius: 50%;
          border: 0.1em solid
            var(--ha-marker-color, var(--default-primary-color));
          color: rgb(76, 76, 76);
          background-color: white;
        }
        iron-image {
          border-radius: 50%;
        }
      </style>

      <div class="marker">
        <template is="dom-if" if="[[entityName]]"
          >[[entityName]]</template
        >
        <template is="dom-if" if="[[entityPicture]]">
          <iron-image
            sizing="cover"
            class="fit"
            src="[[entityPicture]]"
          ></iron-image>
        </template>
      </div>
    `}static get properties(){return{hass:{type:Object},entityId:{type:String,value:""},entityName:{type:String,value:null},entityPicture:{type:String,value:null}}}ready(){super.ready(),this.addEventListener("click",t=>this.badgeTap(t))}badgeTap(t){t.stopPropagation(),this.entityId&&this.fire("hass-more-info",{entityId:this.entityId})}})},678:function(t,e,i){"use strict";i.r(e);i(141);var a=i(4),s=i(26),n=(i(124),i(173),i(387),i(171)),r=i(169),o=i(167),l=i(280);customElements.define("ha-panel-map",class extends(Object(o.a)(s.a)){static get template(){return a.a`
      <style include="ha-style">
        #map {
          height: calc(100% - 64px);
          width: 100%;
          z-index: 0;
        }
      </style>

      <app-toolbar>
        <ha-menu-button></ha-menu-button>
        <div main-title>[[localize('panel.map')]]</div>
      </app-toolbar>

      <div id="map"></div>
    `}static get properties(){return{hass:{type:Object,observer:"drawEntities"}}}connectedCallback(){super.connectedCallback(),this.loadMap()}async loadMap(){[this._map,this.Leaflet]=await Object(l.a)(this.$.map),this.drawEntities(this.hass),this._map.invalidateSize(),this.fitMap()}disconnectedCallback(){this._map&&this._map.remove()}fitMap(){var t;0===this._mapItems.length?this._map.setView(new this.Leaflet.LatLng(this.hass.config.latitude,this.hass.config.longitude),14):(t=new this.Leaflet.latLngBounds(this._mapItems.map(t=>t.getLatLng())),this._map.fitBounds(t.pad(.5)))}drawEntities(t){var e=this._map;if(e){this._mapItems&&this._mapItems.forEach(function(t){t.remove()});var i=this._mapItems=[];Object.keys(t.states).forEach(a=>{var s=t.states[a],o=Object(r.a)(s);if(!(s.attributes.hidden&&"zone"!==Object(n.a)(s)||"home"===s.state)&&"latitude"in s.attributes&&"longitude"in s.attributes){var l;if("zone"===Object(n.a)(s)){if(s.attributes.passive)return;var c="";if(s.attributes.icon){const t=document.createElement("ha-icon");t.setAttribute("icon",s.attributes.icon),c=t.outerHTML}else c=o;return l=this.Leaflet.divIcon({html:c,iconSize:[24,24],className:""}),i.push(this.Leaflet.marker([s.attributes.latitude,s.attributes.longitude],{icon:l,interactive:!1,title:o}).addTo(e)),void i.push(this.Leaflet.circle([s.attributes.latitude,s.attributes.longitude],{interactive:!1,color:"#FF9800",radius:s.attributes.radius}).addTo(e))}var d=s.attributes.entity_picture||"",u=o.split(" ").map(function(t){return t.substr(0,1)}).join("");l=this.Leaflet.divIcon({html:"<ha-entity-marker entity-id='"+s.entity_id+"' entity-name='"+u+"' entity-picture='"+d+"'></ha-entity-marker>",iconSize:[45,45],className:""}),i.push(this.Leaflet.marker([s.attributes.latitude,s.attributes.longitude],{icon:l,title:Object(r.a)(s)}).addTo(e)),s.attributes.gps_accuracy&&i.push(this.Leaflet.circle([s.attributes.latitude,s.attributes.longitude],{interactive:!1,color:"#0288D1",radius:s.attributes.gps_accuracy}).addTo(e))}})}}})}}]);
//# sourceMappingURL=chunk.6b3cf7f7cfb3a37b547c.js.map