/*
 * Combo box definitions
 */

#ifndef __WINE_COMBO_H
#define __WINE_COMBO_H

#define ID_CB_LISTBOX           1000
#define ID_CB_EDIT              1001

/* Internal flags */

#define CBF_DROPPED             0x0001
#define CBF_BUTTONDOWN          0x0002
#define CBF_NOROLLUP            0x0004
#define CBF_MEASUREITEM		0x0008
#define CBF_FOCUSED             0x0010
#define CBF_CAPTURE             0x0020
#define CBF_EDIT                0x0040
#define CBF_NORESIZE		0x0080
#define CBF_NOTIFY		0x0100
#define CBF_EUI                 0x8000

/* Combo state struct */

typedef struct
{
   WND*    	self;
   HWND32  	owner;
   UINT32  	dwStyle;
   HWND32  	hWndEdit;
   HWND32  	hWndLBox;
   UINT16  	wState;
   HFONT16 	hFont;
   RECT16  	RectCombo;
   RECT16  	RectEdit;
   RECT16  	RectButton;
   INT32   	droppedWidth;		/* last two are not used unless set */
   INT32   	editHeight;		/* explicitly */
} HEADCOMBO,*LPHEADCOMBO;

/*
 * Note, that CBS_DROPDOWNLIST style is actually (CBS_SIMPLE | CBS_DROPDOWN)!
 */

#define CB_GETTYPE( lphc )    ((lphc)->dwStyle & (CBS_DROPDOWNLIST))
#define CB_DISABLED( lphc )   ((lphc)->self->dwStyle & WS_DISABLED)
#define CB_OWNERDRAWN( lphc ) ((lphc)->dwStyle & (CBS_OWNERDRAWFIXED | CBS_OWNERDRAWVARIABLE))
#define CB_HASSTRINGS( lphc ) ((lphc)->dwStyle & CBS_HASSTRINGS)
#define CB_HWND( lphc )       ((lphc)->self->hwndSelf)

BOOL32 	COMBO_FlipListbox( LPHEADCOMBO, BOOL32 );
HWND32 	COMBO_GetLBWindow( WND* );
LRESULT COMBO_Directory( LPHEADCOMBO, UINT32, LPSTR, BOOL32 );

#endif /* __WINE_COMBO_H */

