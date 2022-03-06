"use strict";var TokenEx=function(){function o(o,s){function kt(n,t){switch(n){case"load":d=t;break;case"reset":g=t;break;case"focus":nt=t;break;case"blur":tt=t;break;case"change":it=t;break;case"cvvFocus":rt=t;break;case"cvvBlur":ut=t;break;case"cvvChange":ft=t;break;case"tokenize":et=t;break;case"validate":ot=t;break;case"error":w=t;break;case"cardTypeChange":st=t;break;case"notice":p=t;break;case"forterInit":ht=t;break;case"expired":ct=t;break;case"toggleMask":lt=t;break;case"toggleCvvMask":at=t}}function dt(){var n=pt();c.debug=!0;y({valid:n.valid,details:n.details});return}function gt(){var r,n,i;y(c);try{c.customDataTypes!==""&&typeof c.customDataTypes=="string"&&(c.customDataTypes=u(c.customDataTypes))}catch(f){c.debug=!0;y("Error parsing customDataTypes");return}if(r=pt(),!r.valid){c.debug=!0;y({message:"Invalid Config Object",details:r.details});w({error:"Invalid Config Object",details:r.details});return}if(!t(a)){c.debug=!0;y({message:"Invalid Config Object",details:["Invalid container ID property"]});w({error:"Invalid Config Object",details:["Invalid container ID property"]});return}n=document.getElementById("tx_iframe_"+a.id);window.addEventListener?addEventListener("message",b,!1):attachEvent("onmessage",b);t(n)||(n=document.createElement("iframe"),n.setAttribute("src",vt(c.cvvOnly?"CVV":"Data")),n.setAttribute("frameborder","0"),n.setAttribute("width","100%"),n.setAttribute("height","100%"),n.setAttribute("id","tx_iframe_"+a.id),n.setAttribute("name","tx_iframe_"+a.id),a.appendChild(n));c.cvv&&!c.cvvOnly&&(i=document.getElementById("tx_iframe_cvv_"+v.id),t(i)||(i=document.createElement("iframe"),i.setAttribute("src",vt("CVV")),i.setAttribute("frameborder","0"),i.setAttribute("width","100%"),i.setAttribute("height","100%"),i.setAttribute("id","tx_iframe_cvv_"+v.id),i.setAttribute("name","tx_iframe_cvv_"+v.id),v.appendChild(i)));cr()}function vt(n){var t=i+"/iframe/v3?AuthenticationKey="+encodeURIComponent(c.authenticationKey)+"&Origin="+encodeURIComponent(c.origin)+"&TokenExID="+c.tokenExID+"&Timestamp="+c.timestamp+"&Container="+a.id+"&Mode="+n+"&PCI="+(c.pci?"true":"false")+"&EnforceLuhnCompliance="+c.enforceLuhnCompliance;return c.cvvOnly&&(t+="&Token="+c.token+"&CvvOnly=true"),c.cvv&&(t+="&CvvContainer="+c.cvvContainerID,t+="&CVV=true"),c.tokenScheme&&(t+="&TokenScheme="+c.tokenScheme),c.customDataLabel&&(t+="&CustomDataLabel="+c.customDataLabel),c.customCvvDataLabel&&(t+="&CustomCvvDataLabel="+c.customCvvDataLabel),c.title&&(t+="&Title="+encodeURIComponent(c.title)),c.cvvTitle&&(t+="&CvvTitle="+encodeURIComponent(c.cvvTitle)),c.returnKhash&&(t+="&ReturnKhash="+c.returnKhash),c.returnWhash&&(t+="&ReturnWhash="+c.returnWhash),c.expiresInSeconds&&(t+="&ExpiresInSeconds="+c.expiresInSeconds),c.use3DS&&(t+="&Use3ds="+c.use3DS,t+="&ThreeDSMethodNotificationUrl="+c.threeDSMethodNotificationUrl),!c.pci&&c.inputMaxLength&&(t+="&InputMaxLength="+c.inputMaxLength),t}function ni(){c.styles&&fi(c.styles);(c.inputType||c.maskInput&&!c.inputMaxLength)&&ci(c.maskInput?"password":c.inputType);c.pci&&(typeof c.customDataTypes!="undefined"&&c.customDataTypes!==""&&er(c.customDataTypes),c.allowUnknownCardTypes&&ir(),c.enablePrettyFormat&&!c.maskInput&&nr(),c.cvv&&(ai(c.cardType),c.cvvOnly?c.cvvPlaceholder&&yt(c.cvvPlaceholder):(c.cvvPlaceholder&&ui(c.cvvPlaceholder),(c.cvvInputType||c.maskInput)&&li(c.maskInput?"password":c.cvvInputType))),!c.cvvOnly&&c.forterSiteId&&c.forterSiteId.length>0&&c.forterUsername&&c.forterUsername.length>0&&vi(c.forterSiteId,c.forterUsername));!c.pci&&c.customRegEx&&c.customRegEx.length>0&&oi(c.customRegEx);c.placeholder&&yt(c.placeholder);c.enableAutoComplete&&ri();c.enableValidateOnBlur&&si();c.enableAriaRequired&&hi();c.debug&&fr();c.font&&ur(c.font);c.enableValidateOnKeyUp&&tr();c.inputMode&&yi(c.inputMode)}function b(n){var t,r;if(n&&n.data&&n.data!=="undefined"&&n.origin===i&&(t=u(n.data),y(t),t&&t.container&&t.container===a.id))switch(t.event){case"load":ni();d();break;case"cardTypeChange":st(t.data);break;case"focus":nt();break;case"blur":tt();break;case"reset":g();break;case"change":it();break;case"cvvFocus":rt();break;case"cvvBlur":ut();break;case"cvvChange":ft();break;case"error":w(t.data);break;case"validate":ot(t.data);break;case"tokenize":if(et(t.data),c.use3DS){if(r=lr(t.data.threeDSecureResponse,t.data.referenceNumber),r.details.length){y({message:"3DS Device Fingerprinting Failed",details:r.details});p({type:"3DS Device Fingerprinting",success:!1});break}p({type:"3DS Device Fingerprinting",success:!0})}break;case"forterInit":ht(t.data);break;case"expired":ct();break;case"toggleMask":lt(t.data);break;case"toggleCvvMask":at(t.data)}}function ti(){l({command:"tokenize"})}function ii(){l({command:"validate"})}function yt(n){l({command:"setPlaceholder",data:n})}function ri(){l({command:"enableAutoComplete"})}function ui(n){l({command:"setCvvPlaceholder",data:n})}function fi(n){l({command:"setStyle",data:n})}function ei(){l({command:"reset"})}function oi(n){l({command:"setCustomRegEx",data:n})}function si(){l({command:"enableValidateOnBlur"})}function hi(){l({command:"enableAriaRequired"})}function ci(n){l({command:"setType",data:n})}function li(n){l({command:"setCvvType",data:n})}function ai(n){l({command:"setCardType",data:n})}function vi(n,t){l({command:"enableForterIntegration",data:{forterSiteId:n,forterUsername:t}})}function yi(n){l({command:"setInputMode",data:n})}function pi(){l({command:"focus"})}function wi(){l({command:"cvvFocus"})}function bi(){l({command:"toggleMask"})}function ki(){l({command:"toggleCvvMask"})}function di(){l({command:"blur"})}function gi(){l({command:"cvvBlur"})}function nr(){c.pci&&l({command:"enablePrettyFormat"})}function tr(){l({command:"enableValidateOnKeyUp"})}function ir(){c.pci&&l({command:"enableUnknownCardTypes"})}function l(n){var r=document.getElementById("tx_iframe_"+a.id);t(r)&&r.contentWindow.postMessage(JSON.stringify(n),i)}function rr(){var i=document.getElementById("tx_iframe_"+a.id),n;t(i)&&i.parentNode.removeChild(i);v&&(n=document.getElementById("tx_iframe_cvv_"+v.id),t(n)&&n.parentNode.removeChild(n));window.removeEventListener?removeEventListener("message",b,!1):detachEvent("onmessage",b);clearTimeout(r)}function ur(n){l({command:"setFont",data:n})}function fr(){l({command:"enableDebug"})}function er(n){l({command:"setCustomDataTypes",data:n})}function y(n){window.console&&c.debug&&console.log("TokenEx Iframe Debug: "+JSON.stringify(n))}function pt(){var n=[],i,r,t;return(c.origin?(i=c.origin.split(",")[0],f!==i&&n.push("Expected origin of "+i+" but current origin is "+f)):n.push("Missing origin property"),c.tokenExID||n.push("Missing tokenExID property"),isNaN(Number(c.tokenExID))&&n.push("Invalid tokenExID property. TokenExID value must be numeric"),c.tokenScheme||n.push("Missing tokenScheme property"),c.authenticationKey||n.push("Missing authenticationKey property"),c.timestamp||n.push("Missing timestamp property"),c.use3DS)?(c.pci||n.push("Missing pci property"),c.threeDSMethodNotificationUrl.trim()||n.push("Missing threeDSMethodNotificationUrl property"),c.cvvOnly&&n.push("Invalid property cvvOnly for use3DS configuration"),t=n.length===0,{valid:t,details:n}):c.cvvOnly?(c.pci=!0,c.cardType||n.push("Missing cardType property"),c.token||n.push("Missing token property"),t=n.length===0,{valid:t,details:n}):(r=typeof c.customDataTypes!="undefined"&&c.customDataTypes!=="",c.cvv&&!c.cvvOnly)?(c.pci=!0,c.cvvContainerID||n.push("Missing cvvContainerID property"),r&&(wt()||n.push("Unknown custom data type for card type"),sr()||n.push("Invalid card or cvv custom data type")),t=n.length===0,{valid:t,details:n}):c.forterSiteId||c.forterUsername?(c.pci||n.push("Missing pci property"),c.forterSiteId||n.push("Missing forterSiteId property"),c.forterUsername||n.push("Missing forterUsername property"),c.cvvOnly&&n.push("Invalid property cvvOnly for Forter configuration"),t=n.length===0,{valid:t,details:n}):c.pci&&!c.cvv&&!c.cvvOnly&&r?(wt()||n.push("Unknown custom data type for card type"),or()||n.push("Invalid card custom data type"),t=n.length===0,{valid:t,details:n}):(t=n.length===0,{valid:t,details:n})}function wt(){var t,n;try{for(t=c.customDataTypes,n=0;n<t.length;n++)if(t[n].type.toLowerCase()==="unknown")return!1;return!0}catch(i){return!1}}function or(){var t,n;try{for(t=c.customDataTypes,n=0;n<t.length;n++)if(!bt(t[n]))return!1;return!0}catch(i){return!1}}function sr(){var t,n;try{for(t=c.customDataTypes,n=0;n<t.length;n++)if(!bt(t[n])||!hr(t[n]))return!1;return!0}catch(i){return!1}}function bt(n){return typeof n.type!="undefined"&&n.type!==""&&typeof n.validRegex!="undefined"&&n.validRegex!==""&&k(n.validRegex)&&typeof n.possibleRegEx!="undefined"&&n.possibleRegEx!==""&&k(n.possibleRegEx)&&typeof n.maxLength!="undefined"&&n.maxLength!==""&&parseInt(n.maxLength)>0}function hr(n){return typeof n.cvvValidRegex!="undefined"&&n.cvvValidRegex!==""&&k(n.cvvValidRegex)&&typeof n.cvvMaxLength!="undefined"&&n.cvvMaxLength!==""&&parseInt(n.cvvMaxLength)>=0}function k(n){var t=!0,i;try{i=new RegExp(n)}catch(r){t=!1}return t}function cr(){clearTimeout(r);var t=h(c.expiresInSeconds),n="ExpirationWarning";p({type:n,expirationTimeStamp:t});c.expiresInSeconds>60&&(r=setTimeout(function(){p({type:n,secondsRemaining:"60"})},e(c.expiresInSeconds-60)))}function lr(n,t){var f=[],r,u;return!n[0]||!n[0].threeDSMethodURL?(f.push("Device fingerprinting not supported for this PAN","Send 'MethodCompletionIndicator':'3' or 'MethodCompletionIndicator':'ResultUnavailable' within the ThreeDSecure Authentications request."),{details:f}):(r=i+"/iframe/v3/DeviceFingerprint",r+="?AuthenticationKey="+encodeURIComponent(c.authenticationKey),r+="&Origin="+encodeURIComponent(c.origin),r+="&TokenExID="+c.tokenExID,r+="&TokenScheme="+c.tokenScheme,r+="&PCI=true",r+="&Timestamp="+c.timestamp,r+="&CustomerRefNumber="+t,r+="&ThreeDSMethodUrl="+n[0].threeDSMethodURL,r+="&ThreeDSServerTransID="+n[0].threeDSServerTransID,r+="&ThreeDSMethodNotificationUrl="+c.threeDSMethodNotificationUrl,u=document.createElement("iframe"),u.setAttribute("name","tx_iframe_deviceFingerprint"),u.setAttribute("id","tx_iframe_deviceFingerprint"),u.setAttribute("style","display:none"),u.setAttribute("src",r),a.appendChild(u),{details:f})}var a=document.getElementById(o),c=s,v;c.debug=n(c.debug);c.enablePrettyFormat=n(c.enablePrettyFormat);c.maskInput=n(c.maskInput);c.enableValidateOnBlur=n(c.enableValidateOnBlur);c.enableAriaRequired=n(c.enableAriaRequired);c.pci=n(c.pci);c.cvvOnly=n(c.cvvOnly);c.allowUnknownCardTypes=n(c.allowUnknownCardTypes);c.returnKhash=n(c.returnKhash);c.returnWhash=n(c.returnWhash);c.enforceLuhnCompliance=c.enforceLuhnCompliance?n(c.enforceLuhnCompliance):!0;c.use3DS=n(c.use3DS);c.validateOnKeyUp=n(c.enableValidateOnKeyUp);c.expiresInSeconds=parseInt(c.expiresInSeconds)>0&&parseInt(c.expiresInSeconds)<1200?parseInt(c.expiresInSeconds):1200;c.cvv&&(v=document.getElementById(c.cvvContainerID));var d=function(){},g=function(){},nt=function(){},tt=function(){},it=function(){},rt=function(){},ut=function(){},ft=function(){},et=function(){},ot=function(){},w=function(){},st=function(){},p=function(){},ht=function(){},ct=function(){},lt=function(){},at=function(){};return{load:gt,on:kt,tokenize:ti,validate:ii,reset:ei,blur:di,cvvBlur:gi,focus:pi,cvvFocus:wi,remove:rr,toggleMask:bi,toggleCvvMask:ki,validateConfig:dt}}function s(r,f){function k(n,t){switch(n){case"load":a=t;break;case"error":v=t;break;case"expired":y=t}}function d(){var n,i;if(l(e),!ut()){e.debug=!0;l("Invalid Config Object");return}if(!t(o)){e.debug=!0;l("Invalid Container ID");return}n=document.getElementById("tx_iframe_"+o.id);window.addEventListener?addEventListener("message",c,!1):attachEvent("onmessage",c);t(n)||(n=document.createElement("iframe"),n.setAttribute("src",p(e.cvvOnly?"CVV":"Data")),n.setAttribute("frameborder","0"),n.setAttribute("width","100%"),n.setAttribute("height","100%"),n.setAttribute("id","tx_iframe_"+o.id),n.setAttribute("name","tx_iframe_"+o.id),o.appendChild(n));e.cvv&&!e.cvvOnly&&(i=document.getElementById("tx_iframe_cvv_"+s.id),t(i)||(i=document.createElement("iframe"),i.setAttribute("src",p("CVV")),i.setAttribute("frameborder","0"),i.setAttribute("width","100%"),i.setAttribute("height","100%"),i.setAttribute("id","tx_iframe_cvv_"+s.id),i.setAttribute("name","tx_iframe_cvv_"+s.id),s.appendChild(i)))}function p(n){var t=i+"/iframe/v3/detokenize?AuthenticationKey="+encodeURIComponent(e.authenticationKey)+"&Origin="+encodeURIComponent(e.origin)+"&TokenExID="+e.tokenExID+"&Timestamp="+e.timestamp+"&Container="+o.id+"&Token="+encodeURIComponent(e.token)+"&Mode="+n;return e.cvvOnly&&(t+="&CvvOnly=true"),e.cvv&&(t+="&CvvContainer="+e.cvvContainerID,t+="&CVV=true"),e.customDataLabel&&(t+="&CustomDataLabel="+e.customDataLabel),e.customCvvDataLabel&&(t+="&CustomCvvDataLabel="+e.customCvvDataLabel),e.title&&(t+="&Title="+e.title),e.expiresInSeconds&&(t+="&ExpiresInSeconds="+e.expiresInSeconds),t}function g(){e.styles&&nt(e.styles);e.debug&&rt();e.font&&it(e.font)}function c(n){if(n&&n.data&&n.data!=="undefined"&&n.origin===i){var t=u(n.data);if(l(t),t&&t.container&&t.container===o.id)switch(t.event){case"load":g();a();break;case"error":v(t.data);break;case"expired":y();w()}}}function nt(n){h({command:"setStyle",data:n})}function tt(){h({command:"reset"})}function h(n){var r=document.getElementById("tx_iframe_"+o.id);t(r)&&(n.fromIframeV3=!0,r.contentWindow.postMessage(JSON.stringify(n),i))}function w(){var r=document.getElementById("tx_iframe_"+o.id),n,i;t(r)&&r.parentNode.removeChild(r);s&&(n=document.getElementById("tx_iframe_cvv_"+s.id),t(n)&&n.parentNode.removeChild(n));e.use3DS&&(i=document.getElementById("tx_iframe_deviceFingerprint"),t(i)&&i.parentNode.removeChild(i));window.removeEventListener?removeEventListener("message",c,!1):detachEvent("onmessage",c)}function it(n){h({command:"setFont",data:n})}function rt(){h({command:"enableDebug"})}function l(n){window.console&&e.debug&&console.log("TokenEx Iframe Debug: "+JSON.stringify(n))}function ut(){return e.cvvOnly?(e.pci=!0,e.origin&&e.tokenExID&&e.authenticationKey&&e.timestamp&&e.token):e.cvv&&!e.cvvOnly?(e.pci=!0,e.cvvContainerID):e.origin&&e.tokenExID&&e.authenticationKey&&e.timestamp?!0:!1}var o=document.getElementById(r),e=f,s,b=parseInt(e.expiresInSeconds)>60?60:20;e.cvvOnly=n(e.cvvOnly);e.expiresInSeconds=parseInt(e.expiresInSeconds)>0&&parseInt(e.expiresInSeconds)<=60?parseInt(e.expiresInSeconds):b;e.cvv&&(s=document.getElementById(e.cvvContainerID));var a=function(){},v=function(){},y=function(){};return{load:d,on:k,reset:tt,remove:w}}function t(n){return typeof n=="undefined"||n===null?!1:!0}function u(n){try{return JSON.parse(n)}catch(t){return null}}function h(n){return new Date((new Date).getTime()+e(n)).toISOString().replace(/[-T:\.Z]/g,"").slice(0,-3)}function e(n){return n*1e3}function n(n){switch(typeof n){case"string":return n.toLowerCase()==="true";case"number":return n===1;case"boolean":return n;default:return!1}}var i="https://eu1-htp.tokenex.com",f=window.location.origin,r;return{Iframe:o,DetokenizeIframe:s}}();
