name	user32
type	win32
base	1

0000 stub ActivateKeyboardLayout
0001 stdcall AdjustWindowRect(ptr long long) AdjustWindowRect32
0002 stdcall AdjustWindowRectEx(ptr long long long) AdjustWindowRectEx32
0003 stdcall AnyPopup() AnyPopup32
0004 stdcall AppendMenuA(long long long ptr) AppendMenu32A
0005 stdcall AppendMenuW(long long long ptr) AppendMenu32W
0006 stdcall ArrangeIconicWindows(long) ArrangeIconicWindows32
0007 stub AttachThreadInput
0008 stdcall BeginDeferWindowPos(long) BeginDeferWindowPos32
0009 stdcall BeginPaint(long ptr) BeginPaint32
0010 stdcall BringWindowToTop(long) BringWindowToTop32
0011 stub BroadcastSystemMessage
0012 stub CalcChildScroll
0013 stub CallMsgFilter
0014 stdcall CallMsgFilterA(ptr long) CallMsgFilter32A
0015 stdcall CallMsgFilterW(ptr long) CallMsgFilter32W
0016 stdcall CallNextHookEx(long long long long) CallNextHookEx32
0017 stdcall CallWindowProcA(ptr long long long long) CallWindowProc32A
0018 stdcall CallWindowProcW(ptr long long long long) CallWindowProc32W
0019 stub CascadeChildWindows
0020 stub CascadeWindows
0021 stdcall ChangeClipboardChain(long long) ChangeClipboardChain32
0022 stdcall ChangeMenuA(long long ptr long long) ChangeMenu32A
0023 stdcall ChangeMenuW(long long ptr long long) ChangeMenu32W
0024 stdcall CharLowerA(ptr) CharLower32A
0025 stdcall CharLowerBuffA(ptr long) CharLowerBuff32A
0026 stdcall CharLowerBuffW(ptr long) CharLowerBuff32W
0027 stdcall CharLowerW(ptr) CharLower32W
0028 stdcall CharNextA(ptr) CharNext32A
0029 stdcall CharNextExA(long ptr long) CharNextEx32A
0030 stdcall CharNextExW(long ptr long) CharNextEx32W
0031 stdcall CharNextW(ptr) CharNext32W
0032 stdcall CharPrevA(ptr ptr) CharPrev32A
0033 stdcall CharPrevExA(long ptr ptr long) CharPrevEx32A
0034 stdcall CharPrevExW(long ptr ptr long) CharPrevEx32W
0035 stdcall CharPrevW(ptr ptr) CharPrev32W
0036 stdcall CharToOemA(ptr ptr) CharToOem32A
0037 stdcall CharToOemBuffA(ptr ptr long) CharToOemBuff32A
0038 stdcall CharToOemBuffW(ptr ptr long) CharToOemBuff32W
0039 stdcall CharToOemW(ptr ptr) CharToOem32W
0040 stdcall CharUpperA(ptr) CharUpper32A
0041 stdcall CharUpperBuffA(ptr long) CharUpperBuff32A
0042 stdcall CharUpperBuffW(ptr long) CharUpperBuff32W
0043 stdcall CharUpperW(ptr) CharUpper32W
0044 stdcall CheckDlgButton(long long long) CheckDlgButton32
0045 stdcall CheckMenuItem(long long long) CheckMenuItem32
0046 stub CheckMenuRadioItem
0047 stdcall CheckRadioButton(long long long long) CheckRadioButton32
0048 stdcall ChildWindowFromPoint(long long long) ChildWindowFromPoint32
0049 stub ChildWindowFromPointEx
0050 stub ClientThreadConnect
0051 stdcall ClientToScreen(long ptr) ClientToScreen32
0052 stdcall ClipCursor(ptr) ClipCursor32
0053 stdcall CloseClipboard() CloseClipboard32
0054 stub CloseDesktop
0055 stdcall CloseWindow(long) CloseWindow32
0056 stub CloseWindowStation
0057 stub CopyAcceleratorTableA
0058 stub CopyAcceleratorTableW
0059 stdcall CopyIcon(long) CopyIcon32
0060 stdcall CopyImage(long long long long long) CopyImage32
0061 stdcall CopyRect(ptr ptr) CopyRect32
0062 stdcall CountClipboardFormats() CountClipboardFormats32
0063 stub CreateAcceleratorTableA
0064 stub CreateAcceleratorTableW
0065 stdcall CreateCaret(long long long long) CreateCaret32
0066 stdcall CreateCursor(long long long long long ptr ptr) CreateCursor32
0067 stub CreateDesktopA
0068 stub CreateDesktopW
0069 stdcall CreateDialogIndirectParamA(long ptr long ptr long) CreateDialogIndirectParam32A
0070 stub CreateDialogIndirectParamAorW
0071 stdcall CreateDialogIndirectParamW(long ptr long ptr long) CreateDialogIndirectParam32W
0072 stdcall CreateDialogParamA(long ptr long ptr long) CreateDialogParam32A
0073 stdcall CreateDialogParamW(long ptr long ptr long) CreateDialogParam32W
0074 stdcall CreateIcon(long long long long long ptr ptr) CreateIcon32
0075 stub CreateIconFromResource
0076 stub CreateIconFromResourceEx
0077 stub CreateIconIndirect
0078 stub CreateMDIWindowA
0079 stub CreateMDIWindowW
0080 stdcall CreateMenu() CreateMenu32
0081 stdcall CreatePopupMenu() CreatePopupMenu32
0082 stdcall CreateWindowExA(long ptr ptr long long long long long 
				long long long ptr) CreateWindowEx32A
0083 stdcall CreateWindowExW(long ptr ptr long long long long long 
				long long long ptr) CreateWindowEx32W
0084 stub CreateWindowStationA
0085 stub CreateWindowStationW
0086 stub DdeAbandonTransaction
0087 stub DdeAccessData
0088 stub DdeAddData
0089 return DdeClientTransaction 32 0
0090 stub DdeCmpStringHandles
0091 return DdeConnect 16 0
0092 stub DdeConnectList
0093 stub DdeCreateDataHandle
0094 return DdeCreateStringHandleA 12 0
0095 return DdeCreateStringHandleW 12 0
0096 return DdeDisconnect 4 0
0097 stub DdeDisconnectList
0098 stub DdeEnableCallback
0099 return DdeFreeDataHandle 4 1
0100 return DdeFreeStringHandle 8 0
0101 stub DdeGetData
0102 return DdeGetLastError 4 0
0103 stub DdeGetQualityOfService
0104 stub DdeImpersonateClient
0105 return DdeInitializeA 16 0
0106 return DdeInitializeW 16 0
0107 stub DdeKeepStringHandle
0108 return DdeNameService 16 0
0109 stub DdePostAdvise
0110 stub DdeQueryConvInfo
0111 stub DdeQueryNextServer
0112 stub DdeQueryStringA
0113 stub DdeQueryStringW
0114 stub DdeReconnect
0115 stub DdeSetQualityOfService
0116 stub DdeSetUserHandle
0117 stub DdeUnaccessData
0118 return DdeUninitialize 4 0
0119 stdcall DefDlgProcA(long long long long) DefDlgProc32A
0120 stdcall DefDlgProcW(long long long long) DefDlgProc32W
0121 stdcall DefFrameProcA(long long long long long) DefFrameProc32A
0122 stdcall DefFrameProcW(long long long long long) DefFrameProc32W
0123 stdcall DefMDIChildProcA(long long long long) DefMDIChildProc32A
0124 stdcall DefMDIChildProcW(long long long long) DefMDIChildProc32W
0125 stdcall DefWindowProcA(long long long long) DefWindowProc32A
0126 stdcall DefWindowProcW(long long long long) DefWindowProc32W
0127 stdcall DeferWindowPos(long long long long long long long long) DeferWindowPos32
0128 stdcall DeleteMenu(long long long) DeleteMenu32
0129 stub DestroyAcceleratorTable
0130 stdcall DestroyCaret() DestroyCaret32
0131 stdcall DestroyCursor(long) DestroyCursor32
0132 stdcall DestroyIcon(long) DestroyIcon32
0133 stdcall DestroyMenu(long) DestroyMenu32
0134 stdcall DestroyWindow(long) DestroyWindow32
0135 stdcall DialogBoxIndirectParamA(long ptr long ptr long) DialogBoxIndirectParam32A
0136 stdcall DialogBoxIndirectParamAorW(long ptr long ptr long) DialogBoxIndirectParam32A
0137 stdcall DialogBoxIndirectParamW(long ptr long ptr long) DialogBoxIndirectParam32W
0138 stdcall DialogBoxParamA(long ptr long ptr long) DialogBoxParam32A
0139 stdcall DialogBoxParamW(long ptr long ptr long) DialogBoxParam32W
0140 stdcall DispatchMessageA(ptr) DispatchMessage32A
0141 stdcall DispatchMessageW(ptr) DispatchMessage32W
0142 stdcall DlgDirListA(long ptr long long long) DlgDirList32A
0143 stdcall DlgDirListComboBoxA(long ptr long long long) DlgDirListComboBox32A
0144 stdcall DlgDirListComboBoxW(long ptr long long long) DlgDirListComboBox32W
0145 stdcall DlgDirListW(long ptr long long long) DlgDirList32W
0146 stdcall DlgDirSelectComboBoxExA(long ptr long long) DlgDirSelectComboBoxEx32A
0147 stdcall DlgDirSelectComboBoxExW(long ptr long long) DlgDirSelectComboBoxEx32W
0148 stdcall DlgDirSelectExA(long ptr long long) DlgDirSelectEx32A
0149 stdcall DlgDirSelectExW(long ptr long long) DlgDirSelectEx32W
0150 stdcall DragDetect(long long long) DragDetect32
0151 stub DragObject
0152 stdcall DrawAnimatedRects(long long ptr ptr) DrawAnimatedRects32
0153 stub DrawCaption
0154 stdcall DrawEdge(long ptr long long) DrawEdge32
0155 stdcall DrawFocusRect(long ptr) DrawFocusRect32
0156 stub DrawFrame
0157 stdcall DrawFrameControl(long ptr long long) DrawFrameControl32
0158 stdcall DrawIcon(long long long long) DrawIcon32
0159 stub DrawIconEx
0160 stdcall DrawMenuBar(long) DrawMenuBar32
0161 stdcall DrawStateA(long long ptr long long long long long long long) DrawState32A
0162 stub DrawStateW
0163 stdcall DrawTextA(long ptr long ptr long) DrawText32A
0164 stub DrawTextExA
0165 stub DrawTextExW
0166 stdcall DrawTextW(long ptr long ptr long) DrawText32W
0167 stub EditWndProc
0168 stdcall EmptyClipboard() EmptyClipboard32
0169 stdcall EnableMenuItem(long long long) EnableMenuItem32
0170 stdcall EnableScrollBar(long long long) EnableScrollBar32
0171 stdcall EnableWindow(long long) EnableWindow32
0172 stdcall EndDeferWindowPos(long) EndDeferWindowPos32
0173 stdcall EndDialog(long long) EndDialog32
0174 stdcall EndMenu() EndMenu
0175 stdcall EndPaint(long ptr) EndPaint32
0176 stub EndTask
0177 stdcall EnumChildWindows(long ptr long) THUNK_EnumChildWindows32
0178 stdcall EnumClipboardFormats(long) EnumClipboardFormats32
0179 stub EnumDesktopsA
0180 stub EnumDesktopsW
0181 stub EnumDisplayDeviceModesA
0182 stub EnumDisplayDeviceModesW
0183 stub EnumDisplayDevicesA
0184 stub EnumDisplayDevicesW
0185 stdcall EnumPropsA(long ptr) THUNK_EnumProps32A
0186 stdcall EnumPropsExA(long ptr long) THUNK_EnumPropsEx32A
0187 stdcall EnumPropsExW(long ptr long) THUNK_EnumPropsEx32W
0188 stdcall EnumPropsW(long ptr) THUNK_EnumProps32W
0189 stdcall EnumThreadWindows(long ptr long) THUNK_EnumThreadWindows
0190 stub EnumWindowStationsA
0191 stub EnumWindowStationsW
0192 stdcall EnumWindows(ptr long) THUNK_EnumWindows32
0193 stdcall EqualRect(ptr ptr) EqualRect32
0194 stdcall ExcludeUpdateRgn(long long) ExcludeUpdateRgn32
0195 stdcall ExitWindowsEx(long long) ExitWindowsEx
0196 stdcall FillRect(long ptr long) FillRect32
0197 stdcall FindWindowA(ptr ptr) FindWindow32A
0198 stdcall FindWindowExA(long long ptr ptr) FindWindowEx32A
0199 stdcall FindWindowExW(long long ptr ptr) FindWindowEx32W
0200 stdcall FindWindowW(ptr ptr) FindWindow32W
0201 stdcall FlashWindow(long long) FlashWindow32
0202 stdcall FrameRect(long ptr long) FrameRect32
0203 stub FreeDDElParam
0204 stdcall GetActiveWindow() GetActiveWindow32
0205 stdcall GetAppCompatFlags(long) GetAppCompatFlags32
0206 stdcall GetAsyncKeyState(long) GetAsyncKeyState32
0207 stdcall GetCapture() GetCapture32
0208 stdcall GetCaretBlinkTime() GetCaretBlinkTime32
0209 stdcall GetCaretPos(ptr) GetCaretPos32
0210 stdcall GetClassInfoA(long ptr ptr) GetClassInfo32A
0211 stdcall GetClassInfoExA(long ptr ptr) GetClassInfoEx32A
0212 stdcall GetClassInfoExW(long ptr ptr) GetClassInfoEx32W
0213 stdcall GetClassInfoW(long ptr ptr) GetClassInfo32W
0214 stdcall GetClassLongA(long long) GetClassLong32A
0215 stdcall GetClassLongW(long long) GetClassLong32W
0216 stdcall GetClassNameA(long ptr long) GetClassName32A
0217 stdcall GetClassNameW(long ptr long) GetClassName32W
0218 stdcall GetClassWord(long long) GetClassWord32
0219 stdcall GetClientRect(long long) GetClientRect32
0220 stdcall GetClipCursor(ptr) GetClipCursor32
0221 stdcall GetClipboardData(long) GetClipboardData32
0222 stdcall GetClipboardFormatNameA(long ptr long) GetClipboardFormatName32A
0223 stdcall GetClipboardFormatNameW(long ptr long) GetClipboardFormatName32W
0224 stdcall GetClipboardOwner() GetClipboardOwner32
0225 stdcall GetClipboardViewer(long) GetClipboardViewer32
0226 stdcall GetCursor() GetCursor32
0227 stub GetCursorInfo
0228 stdcall GetCursorPos(ptr) GetCursorPos32
0229 stdcall GetDC(long) GetDC32
0230 stdcall GetDCEx(long long long) GetDCEx32
0231 stdcall GetDesktopWindow() GetDesktopWindow32
0232 stdcall GetDialogBaseUnits() GetDialogBaseUnits
0233 stdcall GetDlgCtrlID(long) GetDlgCtrlID32
0234 stdcall GetDlgItem(long long) GetDlgItem32
0235 stdcall GetDlgItemInt(long long ptr long) GetDlgItemInt32
0236 stdcall GetDlgItemTextA(long long ptr long) GetDlgItemText32A
0237 stdcall GetDlgItemTextW(long long ptr long) GetDlgItemText32W
0238 stdcall GetDoubleClickTime() GetDoubleClickTime32
0239 stdcall GetFocus() GetFocus32
0240 return GetForegroundWindow 0 0		#FIXME
0241 stub GetIconInfo
0242 stub GetInputDesktop
0243 stdcall GetInputState() GetInputState32
0244 stdcall GetInternalWindowPos(long ptr ptr) GetInternalWindowPos32
0245 stdcall GetKBCodePage() GetKBCodePage32
0246 stdcall GetKeyNameTextA(long ptr long) GetKeyNameText32A
0247 stdcall GetKeyNameTextW(long ptr long) GetKeyNameText32W
0248 stdcall GetKeyState(long) GetKeyState32
0249 stdcall GetKeyboardLayout(long) GetKeyboardLayout
0250 stub GetKeyboardLayoutList
0251 stub GetKeyboardLayoutNameA
0252 stub GetKeyboardLayoutNameW
0253 stdcall GetKeyboardState(ptr) GetKeyboardState
0254 stdcall GetKeyboardType(long) GetKeyboardType32
0255 stdcall GetLastActivePopup(long) GetLastActivePopup32
0256 stdcall GetMenu(long) GetMenu32
0257 stdcall GetMenuCheckMarkDimensions() GetMenuCheckMarkDimensions
0258 stub GetMenuContextHelpId
0259 stub GetMenuDefaultItem
0260 stub GetMenuIndex
0261 stdcall GetMenuItemCount(long) GetMenuItemCount32
0262 stdcall GetMenuItemID(long long) GetMenuItemID32
0263 stdcall GetMenuItemInfoA(long long long ptr) GetMenuItemInfo32A
0264 stdcall GetMenuItemInfoW(long long long ptr) GetMenuItemInfo32W
0265 stub GetMenuItemRect
0266 stdcall GetMenuState(long long long) GetMenuState32
0267 stdcall GetMenuStringA(long long ptr long long) GetMenuString32A
0268 stdcall GetMenuStringW(long long ptr long long) GetMenuString32W
0269 stdcall GetMessageA(ptr long long long) GetMessage32A
0270 stdcall GetMessageExtraInfo() GetMessageExtraInfo
0271 stdcall GetMessagePos() GetMessagePos
0272 stdcall GetMessageTime() GetMessageTime
0273 stdcall GetMessageW(ptr long long long) GetMessage32W
0274 stdcall GetNextDlgGroupItem(long long long) GetNextDlgGroupItem32
0275 stdcall GetNextDlgTabItem(long long long) GetNextDlgTabItem32
0276 stdcall GetOpenClipboardWindow() GetOpenClipboardWindow32
0277 stdcall GetParent(long) GetParent32
0278 stub GetPriorityClipboardFormat
0279 stub GetProcessWindowStation
0280 stdcall GetPropA(long ptr) GetProp32A
0281 stdcall GetPropW(long ptr) GetProp32W
0282 stub GetQueueStatus
0283 stdcall GetScrollInfo(long long ptr) GetScrollInfo32
0284 stdcall GetScrollPos(long long) GetScrollPos32
0285 stdcall GetScrollRange(long long ptr ptr) GetScrollRange32
0286 return GetShellWindow 0 0
0287 stdcall GetSubMenu(long long) GetSubMenu32
0288 stdcall GetSysColor(long) GetSysColor32
0289 stdcall GetSysColorBrush(long) GetSysColorBrush32
0290 stdcall GetSystemMenu(long long) GetSystemMenu32
0291 stdcall GetSystemMetrics(long) GetSystemMetrics32
0292 stdcall GetTabbedTextExtentA(long ptr long long ptr) GetTabbedTextExtent32A
0293 stdcall GetTabbedTextExtentW(long ptr long long ptr) GetTabbedTextExtent32W
0294 stub GetThreadDesktop
0295 stdcall GetTopWindow(long) GetTopWindow32
0296 stdcall GetUpdateRect(long ptr long) GetUpdateRect32
0297 stdcall GetUpdateRgn(long long long) GetUpdateRgn32
0298 stub GetUserObjectInformationA
0299 stub GetUserObjectInformationW
0300 stub GetUserObjectSecurity
0301 stdcall GetWindow(long long) GetWindow32
0302 stub GetWindowContextHelpId
0303 stdcall GetWindowDC(long) GetWindowDC32
0304 stdcall GetWindowLongA(long long) GetWindowLong32A
0305 stdcall GetWindowLongW(long long) GetWindowLong32W
0306 stdcall GetWindowPlacement(long ptr) GetWindowPlacement32
0307 stdcall GetWindowRect(long ptr) GetWindowRect32
0308 stdcall GetWindowTextA(long ptr long) GetWindowText32A
0309 stdcall GetWindowTextLengthA(long) GetWindowTextLength32A
0310 stdcall GetWindowTextLengthW(long) GetWindowTextLength32W
0311 stdcall GetWindowTextW(long ptr long) GetWindowText32W
0312 stdcall GetWindowThreadProcessId(long ptr) GetWindowThreadProcessId
0313 stdcall GetWindowWord(long long) GetWindowWord32
0314 stdcall GrayStringA(long long ptr long long long long long long) THUNK_GrayString32A
0315 stdcall GrayStringW(long long ptr long long long long long long) THUNK_GrayString32W
0316 stdcall HideCaret(long) HideCaret32
0317 stdcall HiliteMenuItem(long long long long) HiliteMenuItem32
0318 stub ImpersonateDdeClientWindow
0319 stdcall InSendMessage() InSendMessage32
0320 stdcall InflateRect(ptr long long) InflateRect32
0321 stdcall InsertMenuA(long long long long ptr) InsertMenu32A
0322 stdcall InsertMenuItemA(long long long ptr) InsertMenuItem32A
0323 stdcall InsertMenuItemW(long long long ptr) InsertMenuItem32W
0324 stdcall InsertMenuW(long long long long ptr) InsertMenu32W
0325 stub InternalGetWindowText
0326 stdcall IntersectRect(ptr ptr ptr) IntersectRect32
0327 stdcall InvalidateRect(long ptr long) InvalidateRect32
0328 stdcall InvalidateRgn(long long long) InvalidateRgn32
0329 stdcall InvertRect(long ptr) InvertRect32
0330 stdcall IsCharAlphaA(long) IsCharAlpha32A
0331 stdcall IsCharAlphaNumericA(long) IsCharAlphaNumeric32A
0332 stdcall IsCharAlphaNumericW(long) IsCharAlphaNumeric32W
0333 stdcall IsCharAlphaW(long) IsCharAlpha32W
0334 stdcall IsCharLowerA(long) IsCharLower32A
0335 stdcall IsCharLowerW(long) IsCharLower32W
0336 stdcall IsCharUpperA(long) IsCharUpper32A
0337 stdcall IsCharUpperW(long) IsCharUpper32W
0338 stdcall IsChild(long long) IsChild32
0339 stdcall IsClipboardFormatAvailable(long) IsClipboardFormatAvailable32
0340 stub IsDialogMessage
0341 stdcall IsDialogMessageA(long ptr) IsDialogMessage32A
0342 stdcall IsDialogMessageW(long ptr) IsDialogMessage32W
0343 stdcall IsDlgButtonChecked(long long) IsDlgButtonChecked32
0344 stdcall IsIconic(long) IsIconic32
0345 stdcall IsMenu(long) IsMenu32
0346 stdcall IsRectEmpty(ptr) IsRectEmpty32
0347 stdcall IsWindow(long) IsWindow32
0348 stdcall IsWindowEnabled(long) IsWindowEnabled32
0349 stdcall IsWindowUnicode(long) IsWindowUnicode
0350 stdcall IsWindowVisible(long) IsWindowVisible32
0351 stdcall IsZoomed(long) IsZoomed32
0352 stdcall KillSystemTimer(long long) KillSystemTimer32
0353 stdcall KillTimer(long long) KillTimer32
0354 stdcall LoadAcceleratorsA(long ptr) LoadAccelerators32A
0355 stdcall LoadAcceleratorsW(long ptr) LoadAccelerators32W
0356 stdcall LoadBitmapA(long ptr) LoadBitmap32A
0357 stdcall LoadBitmapW(long ptr) LoadBitmap32W
0358 stdcall LoadCursorA(long ptr) LoadCursor32A
0359 stub LoadCursorFromFileA
0360 stub LoadCursorFromFileW
0361 stdcall LoadCursorW(long ptr) LoadCursor32W
0362 stdcall LoadIconA(long ptr) LoadIcon32A
0363 stdcall LoadIconW(long ptr) LoadIcon32W
0364 stdcall LoadImageA(long ptr long long long long) LoadImage32A
0365 stub LoadImageW
0366 stub LoadKeyboardLayoutA
0367 stub LoadKeyboardLayoutW
0368 stub LoadLocalFonts
0369 stdcall LoadMenuA(long ptr) LoadMenu32A
0370 stdcall LoadMenuIndirectA(ptr) LoadMenuIndirect32A
0371 stdcall LoadMenuIndirectW(ptr) LoadMenuIndirect32W
0372 stdcall LoadMenuW(long ptr) LoadMenu32W
0373 stub LoadRemoteFonts
0374 stdcall LoadStringA(long long ptr long) LoadString32A
0375 stdcall LoadStringW(long long ptr long) LoadString32W
0376 stub LockWindowStation
0377 stdcall LockWindowUpdate(long) LockWindowUpdate32
0378 stub LookupIconIdFromDirectory
0379 stub LookupIconIdFromDirectoryEx
0380 stub MBToWCSEx
0381 stdcall MapDialogRect(long ptr) MapDialogRect32
0382 stdcall MapVirtualKeyA(long long) MapVirtualKey32A
0383 stub MapVirtualKeyExA
0384 stdcall MapVirtualKeyW(long long) MapVirtualKey32A
0385 stdcall MapWindowPoints(long long ptr long) MapWindowPoints32
0386 stub MenuItemFromPoint
0387 stub MenuWindowProcA
0388 stub MenuWindowProcW
0389 stdcall MessageBeep(long) MessageBeep32
0390 stdcall MessageBoxA(long ptr ptr long) MessageBox32A
0391 stdcall MessageBoxExA(long ptr ptr long long) MessageBoxEx32A
0392 stdcall MessageBoxExW(long ptr ptr long long) MessageBoxEx32W
0393 stub MessageBoxIndirectA
0394 stub MessageBoxIndirectW
0395 stdcall MessageBoxW(long ptr ptr long) MessageBox32W
0396 stdcall ModifyMenuA(long long long long ptr) ModifyMenu32A
0397 stdcall ModifyMenuW(long long long long ptr) ModifyMenu32W
0398 stdcall MoveWindow(long long long long long long) MoveWindow32
0399 stdcall MsgWaitForMultipleObjects(long ptr long long long) MsgWaitForMultipleObjects
0400 stdcall OemKeyScan(long) OemKeyScan
0401 stdcall OemToCharA(ptr ptr) OemToChar32A
0402 stdcall OemToCharBuffA(ptr ptr long) OemToCharBuff32A
0403 stdcall OemToCharBuffW(ptr ptr long) OemToCharBuff32W
0404 stdcall OemToCharW(ptr ptr) OemToChar32W
0405 stdcall OffsetRect(ptr long long) OffsetRect32
0406 stdcall OpenClipboard(long) OpenClipboard32
0407 stub OpenDesktopA
0408 stub OpenDesktopW
0409 stdcall OpenIcon(long) OpenIcon32
0410 stub OpenInputDesktop
0411 stub OpenWindowStationA
0412 stub OpenWindowStationW
0413 stub PackDDElParam
0414 stub PaintDesktop
0415 stdcall PeekMessageA(ptr long long long long) PeekMessage32A
0416 stdcall PeekMessageW(ptr long long long long) PeekMessage32W
0417 stub PlaySoundEvent
0418 stdcall PostMessageA(long long long long) PostMessage32A
0419 stdcall PostMessageW(long long long long) PostMessage32W
0420 stdcall PostQuitMessage(long) PostQuitMessage32
0421 stub PostThreadMessageA
0422 stub PostThreadMessageW
0423 stdcall PtInRect(ptr long long) PtInRect32
0424 stub QuerySendMessage
0425 stdcall RedrawWindow(long ptr long long) RedrawWindow32
0426 stdcall RegisterClassA(ptr) RegisterClass32A
0427 stdcall RegisterClassExA(ptr) RegisterClassEx32A
0428 stdcall RegisterClassExW(ptr) RegisterClassEx32W
0429 stdcall RegisterClassW(ptr) RegisterClass32W
0430 stdcall RegisterClipboardFormatA(ptr) RegisterClipboardFormat32A
0431 stdcall RegisterClipboardFormatW(ptr) RegisterClipboardFormat32W
0432 stub RegisterHotKey
0433 stub RegisterLogonProcess
0434 stub RegisterSystemThread
0435 stub RegisterTasklist
0436 stdcall RegisterWindowMessageA(ptr) RegisterWindowMessage32A
0437 stdcall RegisterWindowMessageW(ptr) RegisterWindowMessage32W
0438 stdcall ReleaseCapture() ReleaseCapture
0439 stdcall ReleaseDC(long long) ReleaseDC32
0440 stdcall RemoveMenu(long long long) RemoveMenu32
0441 stdcall RemovePropA(long ptr) RemoveProp32A
0442 stdcall RemovePropW(long ptr) RemoveProp32W
0443 stub ReplyMessage
0444 stub ResetDisplay
0445 stub ReuseDDElParam
0446 stdcall ScreenToClient(long ptr) ScreenToClient32
0447 stdcall ScrollChildren(long long long long) ScrollChildren32
0448 stdcall ScrollDC(long long long ptr ptr long ptr) ScrollDC32
0449 stdcall ScrollWindow(long long long ptr ptr) ScrollWindow32
0450 stdcall ScrollWindowEx(long long long ptr ptr long ptr long) ScrollWindowEx32
0451 stdcall SendDlgItemMessageA(long long long long long) SendDlgItemMessage32A
0452 stdcall SendDlgItemMessageW(long long long long long) SendDlgItemMessage32W
0453 stdcall SendMessageA(long long long long) SendMessage32A
0454 stub SendMessageCallbackA
0455 stub SendMessageCallbackW
0456 stub SendMessageTimeoutA
0457 stub SendMessageTimeoutW
0458 stdcall SendMessageW(long long long long) SendMessage32W
0459 stub SendNotifyMessageA
0460 stub SendNotifyMessageW
0461 stub ServerSetFunctionPointers
0462 stdcall SetActiveWindow(long) SetActiveWindow32
0463 stdcall SetCapture(long) SetCapture32
0464 stdcall SetCaretBlinkTime(long) SetCaretBlinkTime32
0465 stdcall SetCaretPos(long long) SetCaretPos32
0466 stdcall SetClassLongA(long long long) SetClassLong32A
0467 stdcall SetClassLongW(long long long) SetClassLong32W
0468 stdcall SetClassWord(long long long) SetClassWord32
0469 stdcall SetClipboardData(long long) SetClipboardData32
0470 stdcall SetClipboardViewer(long) SetClipboardViewer32
0471 stdcall SetCursor(long) SetCursor32
0472 stub SetCursorContents
0473 stdcall SetCursorPos(long long) SetCursorPos32
0474 stub SetDebugErrorLevel
0475 stdcall SetDeskWallPaper(ptr) SetDeskWallPaper32
0476 stdcall SetDlgItemInt(long long long long) SetDlgItemInt32
0477 stdcall SetDlgItemTextA(long long ptr) SetDlgItemText32A
0478 stdcall SetDlgItemTextW(long long ptr) SetDlgItemText32W
0479 stdcall SetDoubleClickTime(long) SetDoubleClickTime32
0480 stdcall SetFocus(long) SetFocus32
0481 return SetForegroundWindow 4 0
0482 stdcall SetInternalWindowPos(long long ptr ptr) SetInternalWindowPos32
0483 stdcall SetKeyboardState(ptr) SetKeyboardState
0484 stdcall SetLastErrorEx(long long) SetLastErrorEx
0485 stub SetLogonNotifyWindow
0486 stdcall SetMenu(long long) SetMenu32
0487 stub SetMenuContextHelpId
0488 stdcall SetMenuDefaultItem(long long long) SetMenuDefaultItem32
0489 stdcall SetMenuItemBitmaps(long long long long long) SetMenuItemBitmaps32
0490 stdcall SetMenuItemInfoA(long long long ptr) SetMenuItemInfo32A
0491 stdcall SetMenuItemInfoW(long long long ptr) SetMenuItemInfo32W
0492 stub SetMessageExtraInfo
0493 stdcall SetMessageQueue(long) SetMessageQueue32
0494 stdcall SetParent(long long) SetParent32
0495 stub SetProcessWindowStation
0496 stdcall SetPropA(long ptr long) SetProp32A
0497 stdcall SetPropW(long ptr long) SetProp32W
0498 stdcall SetRect(ptr long long long long) SetRect32
0499 stdcall SetRectEmpty(ptr) SetRectEmpty32
0500 stdcall SetScrollInfo(long long ptr long) SetScrollInfo32
0501 stdcall SetScrollPos(long long long long) SetScrollPos32
0502 stdcall SetScrollRange(long long long long long) SetScrollRange32
0503 stub SetShellWindow
0504 stdcall SetSysColors(long ptr ptr) SetSysColors32
0505 stub SetSysColorsTemp
0506 stub SetSystemCursor
0507 stdcall SetSystemMenu(long long) SetSystemMenu32
0508 stdcall SetSystemTimer(long long long ptr) SetSystemTimer32
0509 stub SetThreadDesktop
0510 stdcall SetTimer(long long long ptr) SetTimer32
0511 stub SetUserObjectInformationA
0512 stub SetUserObjectInformationW
0513 stub SetUserObjectSecurity
0514 stub SetWindowContextHelpId
0515 stub SetWindowFullScreenState
0516 stdcall SetWindowLongA(long long long) SetWindowLong32A
0517 stdcall SetWindowLongW(long long long) SetWindowLong32W
0518 stdcall SetWindowPlacement(long ptr) SetWindowPlacement32
0519 stdcall SetWindowPos(long long long long long long long) SetWindowPos32
0520 stub SetWindowStationUser
0521 stdcall SetWindowTextA(long ptr) SetWindowText32A
0522 stdcall SetWindowTextW(long ptr) SetWindowText32W
0523 stdcall SetWindowWord(long long long) SetWindowWord32
0524 stdcall SetWindowsHookA(long ptr) SetWindowsHook32A
0525 stdcall SetWindowsHookExA(long long long long) SetWindowsHookEx32A
0526 stdcall SetWindowsHookExW(long long long long) SetWindowsHookEx32W
0527 stdcall SetWindowsHookW(long long long long) SetWindowsHook32W
0528 stdcall ShowCaret(long) ShowCaret32
0529 stdcall ShowCursor(long) ShowCursor32
0530 stdcall ShowOwnedPopups(long long) ShowOwnedPopups32
0531 stdcall ShowScrollBar(long long long) ShowScrollBar32
0532 stub ShowStartGlass
0533 stdcall ShowWindow(long long) ShowWindow32
0534 stub ShowWindowAsync
0535 stdcall SubtractRect(ptr ptr ptr) SubtractRect32
0536 stdcall SwapMouseButton(long) SwapMouseButton32
0537 stub SwitchDesktop
0538 stdcall SwitchToThisWindow(long long) SwitchToThisWindow32
0539 stdcall SystemParametersInfoA(long long ptr long) SystemParametersInfo32A
0540 stdcall SystemParametersInfoW(long long ptr long) SystemParametersInfo32W
0541 stdcall TabbedTextOutA(long long long ptr long long ptr long) TabbedTextOut32A
0542 stdcall TabbedTextOutW(long long long ptr long long ptr long) TabbedTextOut32W
0543 stub TileChildWindows
0544 stub TileWindows
0545 stdcall ToAscii(long long ptr ptr long) ToAscii32
0546 stub ToAsciiEx
0547 stub ToUnicode
0548 stdcall TrackPopupMenu(long long long long long long ptr) TrackPopupMenu32
0549 stdcall TrackPopupMenuEx(long long long long long ptr) TrackPopupMenuEx
0550 stdcall TranslateAccelerator(long long ptr) TranslateAccelerator32
0551 stdcall TranslateAcceleratorA(long long ptr) TranslateAccelerator32
0552 stdcall TranslateAcceleratorW(long long ptr) TranslateAccelerator32
0553 stub TranslateCharsetInfo
0554 stdcall TranslateMDISysAccel(long ptr) TranslateMDISysAccel32
0555 stdcall TranslateMessage(ptr) TranslateMessage32
0556 stdcall UnhookWindowsHook(long ptr) UnhookWindowsHook32
0557 stdcall UnhookWindowsHookEx(long) UnhookWindowsHookEx32
0558 stdcall UnionRect(ptr ptr ptr) UnionRect32
0559 stub UnloadKeyboardLayout
0560 stub UnlockWindowStation
0561 stub UnpackDDElParam
0562 stdcall UnregisterClassA(ptr long) UnregisterClass32A
0563 stdcall UnregisterClassW(ptr long) UnregisterClass32W
0564 stub UnregisterHotKey
0565 stub UpdatePerUserSystemParameters
0566 stdcall UpdateWindow(long) UpdateWindow32
0567 stub UserClientDllInitialize
0568 stub UserRealizePalette
0569 stub UserRegisterWowHandlers
0570 stdcall ValidateRect(long ptr) ValidateRect32
0571 stdcall ValidateRgn(long long) ValidateRgn32
0572 stdcall VkKeyScanA(long) VkKeyScan32A
0573 stub VkKeyScanExA
0574 stub VkKeyScanExW
0575 stdcall VkKeyScanW(long) VkKeyScan32W
0576 stub WaitForInputIdle
0577 stdcall WaitMessage() WaitMessage
0578 stdcall WinHelpA(long ptr long long) WinHelp32A
0579 stdcall WinHelpW(long ptr long long) WinHelp32W
0580 stdcall WindowFromDC(long) WindowFromDC32
0581 stdcall WindowFromPoint(long long) WindowFromPoint32
0582 stub keybd_event
0583 stub mouse_event
0584 stdcall wsprintfA() WIN32_wsprintf32A
0585 stdcall wsprintfW() WIN32_wsprintf32W
0586 stdcall wvsprintfA(ptr ptr ptr) wvsprintf32A
0587 stdcall wvsprintfW(ptr ptr ptr) wvsprintf32W
#late additions
0588 stub ChangeDisplaySettingsA
0589 stub ChangeDisplaySettingsW
0590 stub EnumDesktopWindows
0591 stub EnumDisplaySettingsA
0592 stub EnumDisplaySettingsW
0593 stub GetWindowRgn
0594 stub MapVirtualKeyExW
0595 stub RegisterServicesProcess
0596 stub SetWindowRgn
0597 stub ToUnicodeEx
0598 stub DrawCaptionTempA
0599 stub RegisterNetworkCapabilities
0600 stub WNDPROC_CALLBACK
