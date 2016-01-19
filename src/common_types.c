/* libsoc - Library to handle standardised output files
 * Copyright (C) 2015 Rikard Nordgren
 * 
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 3 of the License, or (at your option) any later version.
 * 
 * his library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, see <http://www.gnu.org/licenses/>.
 */

#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <pharmml/common_types.h>

#define NUMCOLTYPES 37
static char *coltypenames[] = {
    "undefined", "addl", "adm", "arm", "censoring", "cmt", "covariate", "dose", "duration", "dv", "dvid", "epoch",
    "evid", "id", "idv", "ii", "limit", "mdv", "occasion", "rate", "reg", "replicate", "ss", "ssEndTime", "ssPeriod", "time",
    "indivParameter", "popParameter", "randEffect", "residual", "statPrecision", "strataVariable", "structParameter",
    "varParameter_var", "varParameter_stdev", "varParameter_cov", "varParameter_corr"
};

#define NUMVALTYPES 5
static const char *valtypenames[] = { "real", "int", "string", "id", "boolean" }; 
static const char *valtypeelements[] = { "ct:Real", "ct:Int", "ct:String", "ct:Id", NULL }; 


const char *pharmml_columnType_to_string(pharmml_columnType coltype)
{
    if (coltype < NUMCOLTYPES) {
        return coltypenames[coltype];
    } else {
        return coltypenames[0];
    }
}

pharmml_columnType pharmml_string_to_columnType(const char *str)
{
    for (int i = 0; i < NUMCOLTYPES; i++) {
        if (strcmp(str, coltypenames[i]) == 0) {
            return i;
        }
    }

    return PHARMML_COLTYPE_UNDEFINED;
}

const char *pharmml_valueType_to_string(pharmml_valueType valtype)
{
    if (valtype < NUMVALTYPES) {
        return valtypenames[valtype];
    } else {
        return NULL;
    }
}

const char *pharmml_valueType_to_element(pharmml_valueType valtype)
{
    if (valtype < NUMVALTYPES) {
        return valtypeelements[valtype];
    } else {
        return "";
    }
}

pharmml_valueType pharmml_string_to_valueType(const char *str)
{
    for (int i = 0; i < NUMVALTYPES; i++) {
        if (strcmp(str, valtypenames[i]) == 0) {
            return i;
        }
    }

    return PHARMML_VALUETYPE_ERROR;
}

int pharmml_valueType_to_size(pharmml_valueType valtype)
{
    if (valtype == PHARMML_VALUETYPE_REAL) {
        return sizeof(double);
    } else if (valtype == PHARMML_VALUETYPE_INT) {
        return sizeof(long int);
    } else if (valtype == PHARMML_VALUETYPE_STRING || valtype == PHARMML_VALUETYPE_ID) {
        return sizeof(char *);
    } else if (valtype == PHARMML_VALUETYPE_BOOLEAN) {
        return sizeof(bool);
    }
    return sizeof(char *);   // Emergency fallback
}

double pharmml_string_to_double(const char *str)
{
    return atof(str);
}

char *pharmml_double_to_string(double x)
{
    size_t needed = snprintf(NULL, 0, "%f", x) + 1;
    char *buffer = malloc(needed);
    snprintf(buffer, needed, "%f", x);
    return buffer;
}

int pharmml_string_to_int(const char *str)
{
    return atoi(str);
}

char *pharmml_int_to_string(int x)
{
    size_t needed = snprintf(NULL, 0, "%d", x) + 1;
    char *buffer = malloc(needed);
    snprintf(buffer, needed, "%d", x);
    return buffer;
}

char *pharmml_strdup(const char *str)
{
    size_t len = 1 + strlen(str);
    char *p = malloc(len);
    if (p) {
        memcpy(p, str, len);
    }

    return p;
}

char *pharmml_strndup(const char *str, size_t n)
{
    char *p = malloc(n + 1);
    if (p) {
        memcpy(p, str, n);
        p[n] = '\0';
    }

    return p;
}

int pharmml_copy_string_array(char **source, char **dest, int length)
{
    int fail = 0;

    for (int i = 0; i < length; i++) {
        dest[i] = pharmml_strdup(source[i]);
        if (!dest[i]) {
            for (int j = 0; j < i; j++) {
                free(dest[j]);
            }
            fail = 1;
            break;
        }
    }

    return fail;
}

void pharmml_free_string_array(char **array, int length)
{
    for (int i = 0; i < length; i++) {
        free(array[i]);
    }
    free(array);
}
