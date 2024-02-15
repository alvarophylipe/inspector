from typing import List, Dict
from constants import *
from transformers import AutoTokenizer

_tokenizer = AutoTokenizer.from_pretrained(MODEL, 
                                          do_lower_case=DO_LOWER_CASE)

def encode(data: List[str]):
    res = _tokenizer(
        text=data,
        max_length=MAX_LEN,
        padding=PADDING,
        truncation=TRUNCATION,
        add_special_tokens=ADD_SPECIAL_TOKENS,
        return_tensors='pt',
        return_attention_mask=RETURN_ATTENTION_MASK,
        return_token_type_ids=RETURN_TOKEN_TYPE_IDS
    )

    return dict(res)
