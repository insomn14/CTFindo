rule yara {
    strings:
        $op_code0 = {
            B8 ?? 00 00 00
            0F BE C0
            89 C6
        	}
        $op_code1 = { BE 5F 00 00 00  }
    condition:
        $op_code0 or $op_code1
}
