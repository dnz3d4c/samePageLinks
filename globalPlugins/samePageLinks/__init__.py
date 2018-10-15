# -*- coding: utf-8 -*-
# samePageLinks: 내부 링크 알리미 - Firefox, Chrome과 같은 브라우저에서 내부, 외부 링크가 다르게 인지되도록 개선합니다.
# 이 플러그인은 NVDA Github 이슈 중 <NVDA doesn't know a difference between Links and Same Page Links #141>에서 영감을 받아 제작되었으며, 소스의 많은 부분을 참고하였습니다. 이슈에 대한 자세한 내용을 확인하려면 <https://github.com/nvaccess/nvda/issues/141> 페이지를 방문하세요.
# This add-ons covered by GPL 2.0 license
# Copyright 2018 dnz3d4c

import globalPluginHandler
import api
import controlTypes
import scriptHandler
import ui


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def event_gainFocus (self, obj, nextHandler):
		obj=api.getFocusObject()
		value = obj.value
		if (obj.role == controlTypes.ROLE_LINK):
			if value.find("#") > 0:
				ui.message(u"내부 링크")
		nextHandler()
        
    
