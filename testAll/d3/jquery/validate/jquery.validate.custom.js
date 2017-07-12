/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
//中文字两个字节
jQuery.validator.addMethod("byteRangeLength", function (value, element, param) {
    var length = value.length;
    for (var i = 0; i < value.length; i++) {
        if (value.charCodeAt(i) > 127) {
            length++;
        }
    }
    return this.optional(element) || ( length >= param[0] && length <= param[1] );
}, $.validator.format("文字内容在 {0} 至 {1} 个字节之间(一个中文字符算2个字节)"));

// 邮政编码验证
jQuery.validator.addMethod("isZipCode", function (value, element) {
    var tel = /^[0-9]{6}$/;
    return this.optional(element) || (tel.test(value));
}, "邮政编码不正确");

//手机号码验证
jQuery.validator.addMethod("isMobile", function (value, element) {
    var length = value.length;
    var result = false;
    var mobile = /^(((13[0-9]{1})|(14[0-9]{1})|(15[0-9]{1})|(17[0-9]{1})|(18[0-9]{1}))+\d{8})$/;
    if ($(element).data("sendMsg")) {
        var $sendPhoneCode = $(element).next(".input-group-btn").find(".btn-primary");
        if (this.optional(element) || (mobile.test(value))) {
            result = true;
            $sendPhoneCode.removeAttr('disabled');

        } else {
            result = false;
            $sendPhoneCode.attr('disabled', true);
        }

    } else {
        result = this.optional(element) || (mobile.test(value));
    }

    return result;

}, "手机号码不正确");
//固定电话验证
jQuery.validator.addMethod("isTel", function (value, element) {
    var length = value.length;
    var tel = /^\d{3,4}-?\d{7,8}$/;
    return this.optional(element) || (length == 12 && tel.test(value));
}, "电话号码不正确");
//联系电话（手机话或固定电话）
jQuery.validator.addMethod("isPhone", function (value, element) {
    var tel = /^\d{3,4}-?\d{7,8}$/;
    var mobile = /^(((13[0-9]{1})|(15[0-9]{1})|(17[0-9]{1})|(18[0-9]{1}))+\d{8})$/;
    return this.optional(element) || (mobile.test(value)) || (tel.test(value));
}, "电话号码不正确");

//验证日期和格式是否正确(2009-12-12)
jQuery.validator.addMethod("isDate", function (value, element) {
    var reg = /^(?:(?!0000)[0-9]{4}-(?:(?:0[1-9]|1[0-2])-(?:0[1-9]|1[0-9]|2[0-8])|(?:0[13-9]|1[0-2])-(?:29|30)|(?:0[13578]|1[02])-31)|(?:[0-9]{2}(?:0[48]|[2468][048]|[13579][26])|(?:0[48]|[2468][048]|[13579][26])00)-02-29)$/;
    return this.optional(element) || reg.test(value);
}, "日期格式不正确");
//验证日期和格式是否正确(2009-12-12 00:00:00)
jQuery.validator.addMethod("isDateTime", function (value, element) {
    var reg = /(\d+)-(\d{1,2})-(\d{1,2}) (\d{1,2}):(\d{1,2}):(\d{1,2})$/;
    return this.optional(element) || reg.test(value);
}, "日期格式不正确");

// 验证真实姓名
jQuery.validator.addMethod("isFullName", function (value, element) {
    var reg = /^[\u4e00-\u9fa5A-Za-z0-9_.]*$/;
    return this.optional(element) || reg.test(value);
}, "只能输入中文、英文字母、数字和下划线");

// 验证结束日期不能小于开始日期
jQuery.validator.addMethod("dateCompare", function (value, element, param) {
    var d1 = $(param).val();
    var d2 = $(element).val();
    var beginTimes = d1.substring(0, 10).split('-');
    var endTimes = d2.substring(0, 10).split('-');
    d1 = beginTimes[1] + '/' + beginTimes[2] + '/' + beginTimes[0] + ' ' + d1.substring(10, 19);
    d2 = endTimes[1] + '/' + endTimes[2] + '/' + endTimes[0] + ' ' + d2.substring(10, 19); // -火狐不支持
    var a = (Date.parse(d1) - Date.parse(d2)) / 3600 / 1000;
    return a < 0;
}, "开始时间必须小于结束时间。");

// 验证后面人数必须大于前面人数
jQuery.validator.addMethod("numCompare", function (value, element, param) {
    if (value != "") {
        return parseInt($(param).val()) <= parseInt(value);
    }
    return true;
}, "参加限制人数小的写在前。");

// 验证输入框是否是数字
jQuery.validator.addMethod("isNumber", function (value, element, param) {
    var reg = /^[\d].*$/;
    return this.optional(element) || reg.test(value);
}, "请输入数字。");

// 身份证号码验证
jQuery.validator.addMethod("isIdCardNo", function (value, element) {
    return this.optional(element) || isIdCardNo(value);
}, "请正确输入您的身份证号码");


// 字符验证
jQuery.validator.addMethod("stringCheck", function (value, element) {
    var name = /^[\u4e00-\u9fa5A-Za-z0-9_]+$/;
    return this.optional(element) || (name.test(value));
}, "只能输入中文、英文字母、数字和下划线!");


// 头尾不包含空格
jQuery.validator.addMethod("spaceCheck", function (value, element) {
    var name = /^[^ ]+[\s\S]*[^ ]+$/;
    return this.optional(element) || (name.test(value));
}, "不能以空格开始和结尾！ ");

//登录名必须是数字或字母，不能有特殊字符
jQuery.validator.addMethod("signinNameFomart", function (value, element) {
    var tel = /^\w+$/;
    return this.optional(element) || (tel.test(value));
}, "登录名必须是英文字母或数字或_组成！");

// 验证注册邮箱是否存在
jQuery.validator.addMethod("uniqueValidateEmail", function (value, element) {
    var result = false;
    var ovalue = $(element).data("ovalue");
    if (value !== ovalue) {
        $(element).addClass('loading');
        $.ajax({
            type: "POST",
            url: "/users/uniqueValidate",
            async: false,
            data: {
                'targetType': "email",
                'targetValue': value
            },
            dataType: "json",
            success: function (res) {
                result = res.success;
                $(element).removeClass('loading');
            }
        });
    } else {
        result = true;
    }
    return result;
}, "该邮箱已被注册，<a href='/users/loginView'>登录？</a> 或者<a href='/users/findPassword/forgetPasswordView'>找回密码</a>");
//验证登陆电话
jQuery.validator.addMethod("uniqueValidatePhone", function (value, element) {
    var result = false;
    var ovalue = $(element).data("ovalue");
    if (value != ovalue) {
        $(element).addClass('loading');
        $.ajax({
            type: "POST",
            url: "/users/uniqueValidate",
            async: false,
            dataType: "json",
            data: {
                'targetType': "phone",
                'targetValue': value
            },
            success: function (res) {
                result = res.success;
                $(element).removeClass('loading');
            }
        });
    } else {
        result = true;
    }
    return result;
}, "该电话已被注册账号，<a href='/account/signin'>登录？</a> 或者<a href='/account/forget/password'>找回密码</a>");
//验证邮箱格式
jQuery.validator.addMethod("isEmail", function (value, element) {
    var tel = /\w@\w*\.\w/;
    //var tel = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
    return this.optional(element) || (tel.test(value));
}, "email格式不正确");
//验证绑定邮箱
jQuery.validator.addMethod("bindValidateEmail", function (value, element) {
    var result = false;
    var ovalue = $(element).data("ovalue");
    if (value != ovalue) {
        $(element).addClass('loading');
        $.ajax({
            type: "POST",
            url: "/users/checkEmail",
            async: false,
            data: {
                'email': value
            },
            dataType: "json",
            success: function (res) {
                result = res.success;
                $(element).removeClass('loading');
            }
        });
    } else {
        result = true;
    }
    return result;
}, "该email已被绑定，请重新输入");
//验证登陆名称
jQuery.validator.addMethod("uniqueValidateAccount", function (value, element) {
    var result = false;
    var ovalue = $(element).data("ovalue");
    if (value !== ovalue) {
        $(element).addClass('loading');
        $.ajax({
            type: "POST",
            url: "/users/uniqueValidate",
            async: false,
            data: {
                'targetType': "account",
                'targetValue': value
            },
            dataType: "json",
            success: function (res) {
                result = res.success;
                $(element).removeClass('loading');
            }
        });
    } else {
        result = true;
    }
    return result;
}, "该账号已被注册!");
/**
 * 身份证号码验证
 *
 */
function isIdCardNo(num) {

    var factorArr = new Array(7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1);
    var parityBit = new Array("1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2");
    var varArray = new Array();
    var intValue;
    var lngProduct = 0;
    var intCheckDigit;
    var intStrLen = num.length;
    var idNumber = num;
// initialize
    if ((intStrLen != 15) && (intStrLen != 18)) {
        return false;
    }
// check and set value
    for (i = 0; i < intStrLen; i++) {
        varArray[i] = idNumber.charAt(i);
        if ((varArray[i] < '0' || varArray[i] > '9') && (i != 17)) {
            return false;
        } else if (i < 17) {
            varArray[i] = varArray[i] * factorArr[i];
        }
    }

    if (intStrLen == 18) {
//check date
        var date8 = idNumber.substring(6, 14);
        if (isDate8(date8) == false) {
            return false;
        }
// calculate the sum of the products
        for (i = 0; i < 17; i++) {
            lngProduct = lngProduct + varArray[i];
        }
// calculate the check digit
        intCheckDigit = parityBit[lngProduct % 11];
// check last digit
        if (varArray[17] != intCheckDigit) {
            return false;
        }
    }
    else { //length is 15
//check date
        var date6 = idNumber.substring(6, 12);
        if (isDate6(date6) == false) {

            return false;
        }
    }
    return true;

}


/**
 * 判断是否为“YYYYMM”式的时期
 *
 */
function isDate6(sDate) {
    if (!/^[0-9]{6}$/.test(sDate)) {
        return false;
    }
    var year, month, day;
    year = sDate.substring(0, 4);
    month = sDate.substring(4, 6);
    if (year < 1700 || year > 2500) return false
    if (month < 1 || month > 12) return false
    return true
}
/**
 * 判断是否为“YYYYMMDD”式的时期
 *
 */
function isDate8(sDate) {
    if (!/^[0-9]{8}$/.test(sDate)) {
        return false;
    }
    var year, month, day;
    year = sDate.substring(0, 4);
    month = sDate.substring(4, 6);
    day = sDate.substring(6, 8);
    var iaMonthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year < 1700 || year > 2500) return false
    if (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0)) iaMonthDays[1] = 29;
    if (month < 1 || month > 12) return false
    if (day < 1 || day > iaMonthDays[month - 1]) return false
    return true
}
//验证当前密码
jQuery.validator.addMethod("updateValidatePwd", function (value, element) {
    var result = false;
    var ovalue = $(element).data("ovalue");
    if (value != ovalue) {
        $(element).addClass('loading');
        $.ajax({
            type: "POST",
            url: "/userInfo/updateValidatePwd",
            async: false,
            data: {
                'pwd': value
            },
            dataType: "json",
            success: function (res) {
                result = res.success;
                $(element).removeClass('loading');
            }
        });
    } else {
        result = true;
    }
    return result;
}, "该密码错误，请重新输入");
//密码必须是6-20个英文字母、数字，不能是纯数字
jQuery.validator.addMethod("isPwd", function (value, element) {
    var tel = /^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,20}$/;
    return this.optional(element) || (tel.test(value));
}, "密码必须是6-20个英文字母、数字，不能是纯数字");
//验证选中的组织机构是否有管理员
jQuery.validator.addMethod("checkSelectOrg", function (value, element) {
    var result = false;
    var ovalue = $(element).data("ovalue");
    if (value != ovalue) {
        $(element).addClass('loading');
        $.ajax({
            type: "POST",
            url: "/userManager/checkSelectOrg",
            async: false,
            data: {
                'orgId': value
            },
            dataType: "json",
            success: function (res) {
                result = res.success;
                $(element).removeClass('loading');
            }
        });
    } else {
        result = true;
    }
    return result;
}, "该组织机构已经存在管理员");







