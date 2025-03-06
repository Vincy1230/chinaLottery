import re
from enum import Enum


__all__ = [
    "LotteryBrand",
    "LotteryType",
    "match_lottery_brand",
    "match_lottery_type",
]


# 字符串列表的笛卡尔积
def _product(l1: list[str], l2: list[str]) -> list[str]:
    return [i + j for i in l1 for j in l2]


# 文本归一化：转为小写，并去除中文、英文、数字以外的字符
def _normalize_text(text: str) -> str:
    return re.sub(r"[^\u4e00-\u9fa5a-z0-9]", "", text.lower())


# 彩票品牌枚举
class LotteryBrand(Enum):
    FUCai = "福彩"
    TIcai = "体彩"


# 彩票种类枚举
class LotteryType(Enum):
    F_ShuangSeQiu = "双色球"
    F_3D = "3D"
    F_KuaiLe8 = "快乐8"
    F_QiLeCai = "七乐彩"
    T_DaLeTou = "大乐透"
    T_PaiLie3 = "排列3"
    T_PaiLie5 = "排列5"
    T_QiXingCai = "七星彩"


# 为每个彩票品牌配置特征别名（包括可能的别名、缩写、拼音、混合形式）
LOTTERY_BRAND_ALIASES = {
    LotteryBrand.FUCai: ["福彩", "福", "fu", "fc", "wel"],
    LotteryBrand.TIcai: ["体彩", "体", "ti", "tc", "sport"],
}


# 为每个彩票种类配置特征别名（包括可能的别名、缩写、拼音、混合形式）
LOTTERY_TYPE_ALIASES = {
    LotteryType.F_ShuangSeQiu: ["双色球", "双色", "shuangse", "ssq", "double"],
    LotteryType.F_3D: _product(["三", "3", "san", "s", "three"], ["d"]),
    LotteryType.F_KuaiLe8: _product(
        ["快乐", "kuaile", "kl", "happy", "joy"], ["8", "八", "b", "eight"]
    ),
    LotteryType.F_QiLeCai: _product(
        ["七", "7", "qi", "q", "seven"], ["乐", "le", "lc", "happy", "joy"]
    ),
    LotteryType.T_DaLeTou: ["大乐透", "乐透", "letou", "dlt", "super"],
    LotteryType.T_PaiLie3: _product(
        ["排列", "pailie", "pl", "pick"], ["3", "三", "s", "three"]
    ),
    LotteryType.T_PaiLie5: _product(
        ["排列", "pailie", "pl", "pick"], ["5", "五", "w", "five"]
    ),
    LotteryType.T_QiXingCai: _product(
        ["七", "7", "qi", "q", "seven"], ["星", "xing", "xc", "star"]
    ),
}


# TEST
if __name__ == "__main__":
    # 测试: 列举所有 LOTTERY_TYPE_ALIASES 中的候选名称，检查是否有重复
    all_aliases = []
    for aliases in LOTTERY_BRAND_ALIASES.values():
        all_aliases.extend(aliases)
    for aliases in LOTTERY_TYPE_ALIASES.values():
        all_aliases.extend(aliases)
    print("all_aliases:", all_aliases)
    assert len(all_aliases) == len(set(all_aliases)), "存在重复的彩种别名！"


def match_lottery_brand(user_input: str) -> LotteryBrand | None:
    for brand, aliases in LOTTERY_BRAND_ALIASES.items():
        if any(alias in _normalize_text(user_input) for alias in aliases):
            return brand
    return None


def match_lottery_type(user_input: str) -> LotteryType | None:
    for lottery_type, aliases in LOTTERY_TYPE_ALIASES.items():
        if any(alias in _normalize_text(user_input) for alias in aliases):
            return lottery_type
    return None
