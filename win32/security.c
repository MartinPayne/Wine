#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "windows.h"
#include "ntdll.h"
#include "xmalloc.h"
#include "stddebug.h"
#include "debug.h"

BOOL32 WINAPI IsValidSid (LPSID pSid);
BOOL32 WINAPI EqualSid (LPSID pSid1, LPSID pSid2);
BOOL32 WINAPI EqualPrefixSid (LPSID pSid1, LPSID pSid2);
DWORD  WINAPI GetSidLengthRequired (BYTE nSubAuthorityCount);
BOOL32 WINAPI AllocateAndInitializeSid(LPSID_IDENTIFIER_AUTHORITY pIdentifierAuthority, BYTE nSubAuthorityCount, DWORD nSubAuthority0, DWORD nSubAuthority1, DWORD nSubAuthority2, DWORD nSubAuthority3,    DWORD nSubAuthority4, DWORD nSubAuthority5, DWORD nSubAuthority6, DWORD nSubAuthority7, LPSID *pSid);
VOID*  WINAPI FreeSid(LPSID pSid);
BOOL32 WINAPI InitializeSid (LPSID pSid, LPSID_IDENTIFIER_AUTHORITY pIdentifierAuthority, BYTE nSubAuthorityCount);
LPSID_IDENTIFIER_AUTHORITY WINAPI GetSidIdentifierAuthority(LPSID pSid);
DWORD* WINAPI GetSidSubAuthority(LPSID pSid, DWORD nSubAuthority);
BYTE*  WINAPI GetSidSubAuthorityCount(LPSID pSid);
DWORD  WINAPI GetLengthSid(LPSID pSid);
BOOL32 WINAPI CopySid(DWORD nDestinationSidLength, LPSID pDestinationSid, LPSID pSourceSid);

/***********************************************************************
 *           IsValidSid  (ADVAPI.80)
 */
BOOL32 WINAPI IsValidSid (LPSID pSid) {
    if (!pSid || pSid->Revision != SID_REVISION)
        return FALSE;

    return TRUE;
}

/***********************************************************************
 *           EqualSid  (ADVAPI.40)
 */
BOOL32 WINAPI EqualSid (LPSID pSid1, LPSID pSid2) {
    if (!IsValidSid(pSid1) || !IsValidSid(pSid2))
        return FALSE;

    if (*GetSidSubAuthorityCount(pSid1) != *GetSidSubAuthorityCount(pSid2))
        return FALSE;

    if (memcmp(pSid1, pSid2, GetLengthSid(pSid1)) != 0)
        return FALSE;

    return TRUE;
}

/***********************************************************************
 *           EqualPrefixSid  (ADVAPI.39)
 */
BOOL32 WINAPI EqualPrefixSid (LPSID pSid1, LPSID pSid2) {
    if (!IsValidSid(pSid1) || !IsValidSid(pSid2))
        return FALSE;

    if (*GetSidSubAuthorityCount(pSid1) != *GetSidSubAuthorityCount(pSid2))
        return FALSE;

    if (memcmp(pSid1, pSid2, GetSidLengthRequired(pSid1->SubAuthorityCount - 1))
 != 0)
        return FALSE;

    return TRUE;
}

/***********************************************************************
 *           GetSidLengthRequired  (ADVAPI.63)
 */
DWORD WINAPI GetSidLengthRequired (BYTE nSubAuthorityCount) {
    return sizeof (SID) + (nSubAuthorityCount - 1 * sizeof (DWORD));
}

/***********************************************************************
 *           AllocateAndInitializeSid  (ADVAPI.11)
 */
BOOL32 WINAPI AllocateAndInitializeSid(LPSID_IDENTIFIER_AUTHORITY pIdentifierAuthority,
    BYTE nSubAuthorityCount,
    DWORD nSubAuthority0, DWORD nSubAuthority1,
    DWORD nSubAuthority2, DWORD nSubAuthority3,
    DWORD nSubAuthority4, DWORD nSubAuthority5,
    DWORD nSubAuthority6, DWORD nSubAuthority7,
    LPSID *pSid) {

    *pSid = xmalloc(GetSidLengthRequired(nSubAuthorityCount));
    (*pSid)->Revision = SID_REVISION;
    if (pIdentifierAuthority)
        memcpy(&(*pSid)->IdentifierAuthority, pIdentifierAuthority,
               sizeof (SID_IDENTIFIER_AUTHORITY));
    *GetSidSubAuthorityCount(*pSid) = nSubAuthorityCount;

    if (nSubAuthorityCount > 0)
        *GetSidSubAuthority(*pSid, 0) = nSubAuthority0;
    if (nSubAuthorityCount > 1)
        *GetSidSubAuthority(*pSid, 1) = nSubAuthority1;
    if (nSubAuthorityCount > 2)
        *GetSidSubAuthority(*pSid, 2) = nSubAuthority2;
    if (nSubAuthorityCount > 3)
        *GetSidSubAuthority(*pSid, 3) = nSubAuthority3;
    if (nSubAuthorityCount > 4)
        *GetSidSubAuthority(*pSid, 4) = nSubAuthority4;
    if (nSubAuthorityCount > 5)
        *GetSidSubAuthority(*pSid, 5) = nSubAuthority5;
    if (nSubAuthorityCount > 6)
        *GetSidSubAuthority(*pSid, 6) = nSubAuthority6;
    if (nSubAuthorityCount > 7)
        *GetSidSubAuthority(*pSid, 7) = nSubAuthority7;

    return TRUE;
}

/***********************************************************************
 *           FreeSid  (ADVAPI.42)
 */
VOID* WINAPI FreeSid(LPSID pSid) {
    free(pSid);
    return NULL;
}

/***********************************************************************
 *           InitializeSid  (ADVAPI.74)
 */
BOOL32 WINAPI InitializeSid (LPSID pSid, LPSID_IDENTIFIER_AUTHORITY pIdentifierAuthority,
                    BYTE nSubAuthorityCount)
{
    int i;

    pSid->Revision = SID_REVISION;
    if (pIdentifierAuthority)
        memcpy(&pSid->IdentifierAuthority, pIdentifierAuthority,
               sizeof (SID_IDENTIFIER_AUTHORITY));
    *GetSidSubAuthorityCount(pSid) = nSubAuthorityCount;

    for (i = 0; i < nSubAuthorityCount; i++)
        *GetSidSubAuthority(pSid, i) = 0;

    return TRUE;
}

/***********************************************************************
 *           GetSidIdentifierAuthority  (ADVAPI.62)
 */
LPSID_IDENTIFIER_AUTHORITY WINAPI GetSidIdentifierAuthority (LPSID pSid)
{
    return &pSid->IdentifierAuthority;
}

/***********************************************************************
 *           GetSidSubAuthority  (ADVAPI.64)
 */
DWORD * WINAPI GetSidSubAuthority (LPSID pSid, DWORD nSubAuthority)
{
    return &pSid->SubAuthority[nSubAuthority];
}

/***********************************************************************
 *           GetSidSubAuthorityCount  (ADVAPI.65)
 */
BYTE * WINAPI GetSidSubAuthorityCount (LPSID pSid)
{
    return &pSid->SubAuthorityCount;
}

/***********************************************************************
 *           GetLengthSid  (ADVAPI.48)
 */
DWORD WINAPI GetLengthSid (LPSID pSid)
{
    return GetSidLengthRequired(*GetSidSubAuthorityCount(pSid));
}

/***********************************************************************
 *           CopySid  (ADVAPI.24)
 */
BOOL32 WINAPI CopySid (DWORD nDestinationSidLength, LPSID pDestinationSid,
                       LPSID pSourceSid)
{

    if (!IsValidSid(pSourceSid))
        return FALSE;

    if (nDestinationSidLength < GetLengthSid(pSourceSid))
        return FALSE;

    memcpy(pDestinationSid, pSourceSid, GetLengthSid(pSourceSid));

    return TRUE;
}
