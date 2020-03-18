(window.webpackJsonpBolt4=window.webpackJsonpBolt4||[]).push([[5],{110:function(e,t,i){"use strict";i.r(t);i(89);var n=i(91),o=i(88),r=i(92),s=i(85);function g(e,t){var i=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),i.push.apply(i,n)}return i}function a(e,t,i){return t in e?Object.defineProperty(e,t,{value:i,enumerable:!0,configurable:!0,writable:!0}):e[t]=i,e}var c=new(i(30).a)("GLOBAL-PLAYLIST-HELPER");t.default={configure:function(e,t){for(var i in t.settings)t.settings.hasOwnProperty(i)&&void 0===e.config.settings[i]&&("defaultHD"===i?e.config.settings.defaultHd=t.settings[i]:e.config.settings[i]=t.settings[i]);return t.settings&&c.debug("Create embed settings from playlist settings",t.settings),e.config.playlist=t.playlist,void 0===e.config.settings.advertising&&t.advertising&&(e.config.settings.advertising="true"===t.advertising.on?"on":"off",c.debug("Embed advertising settings from playlist settings:",e.config.settings.advertising)),e.config.playlist},loadPlaylistVideo:function(e,t,i){var d=i.embed,f=d.config.playlist[t].config;if(null===f)return c.error("Cannot load playlist video config (URL null)"),i._showError("Invalid configuration file"),i.iframeReadyCallback.call(null,i),null;c.info("Load playlist video",{url:f});Object(r.a)({url:f,method:"get",timestamp:Date.now()}).then((function(e){var t=e.data,r=e.countryCode;if(t){var f,l,v,u="string"==typeof t?JSON.parse(t):t,p=Object(s.e)("boltCC");if(p?r=p:window.Bolt.userCountryCode||"string"==typeof r&&2===r.trim().length||(r="US"),window.Bolt.userCountryCode=r,(null===(f=u.advertising)||void 0===f?void 0:f.servers)&&(u.advertising.servers=o.a.getSingleAdServerFromServers(u.advertising.servers)),window.PageOS)n.a.sendGDPRInfoToPageOS(null===(l=u.advertising)||void 0===l?void 0:null===(v=l.servers[0])||void 0===v?void 0:v.tags,r,d.config.id);for(var y in u.advertising&&window.BoltAdBlockDetector.detected&&(u.advertising.on=!1),d.config.video=u,d.config=function(e){for(var t=1;t<arguments.length;t++){var i=null!=arguments[t]?arguments[t]:{};t%2?g(Object(i),!0).forEach((function(t){a(e,t,i[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(i)):g(Object(i)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(i,t))}))}return e}({},u,{},d.config),d.config.appearance=u.settings.appearance,Object(s.a)(d.config.video.settings.appearance),i._applyOverrides(d.config.video),d.config.video.settings.hasOwnProperty("defaultHD")&&(d.config.video.settings.defaultHd=d.config.video.settings.defaultHD,delete d.config.video.settings.defaultHD),c.info("Playlist video config",u),d.config.video.settings)d.config.video.settings.hasOwnProperty(y)&&"title"!==y&&"minAge"!==y&&"poster"!==y&&"loop"!==y&&"appearance"!==y&&void 0===d.config.settings[y]&&(d.config.settings[y]=d.config.video.settings[y]);void 0!==d.config.video.settings.minAge&&d.config.video.settings.minAge>0||i._showPoster(d.config.video.content.poster,d.renderer.container),i.jsonConfig=d.config,n.a.setup(i)}}))}}}}]);