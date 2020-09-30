void randomVal(int64_t arg1)
{
    int64_t in_FS_OFFSET;
    int64_t var_48h;
    int64_t fildes;
    void *var_28h;
    int64_t var_20h;
    int64_t var_18h;
    int64_t canary;
    
    canary = *(int64_t *)(in_FS_OFFSET + 0x28);
    fildes._0_4_ = sym.imp.open(0xcd5, 0);        // /dev/urandom
    sym.imp.read((undefined4)fildes, (int64_t)&fildes + 4, 0x20, (int64_t)&fildes + 4);
    sym.imp.close((undefined4)fildes);
    *(int64_t *)arg1 = stack0xffffffffffffffc8;
    *(void **)(arg1 + 8) = var_28h;
    *(int64_t *)(arg1 + 0x10) = var_20h;
    *(int64_t *)(arg1 + 0x18) = var_18h;
    if (canary != *(int64_t *)(in_FS_OFFSET + 0x28)) {
    // WARNING: Subroutine does not return
        sym.imp.__stack_chk_fail();
    }
    return;
}


undefined8 fillArr(void)
{
    undefined8 I;
    
    I = 0;
    while (I < 0x100) {
        *(FillArray + I) = I;
        I = I + 1;
    }
    *VAR_1 = 0;
    *VAR_2 = 0;
    return 1;
}

void swapVal(int64_t arg1, int64_t arg2)
{
    ...    
    uVar1 = *(undefined *)arg1;
    *(undefined *)arg1 = *(undefined *)arg2;
    *(undefined *)arg2 = uVar1;
    return;
}

undefined getValFromArr(void)
{
    uint32_t uVar1;
    
    uVar1 = (*VAR_2 + 1 >> 0x1f) >> 0x18;
    *VAR_2 = (*VAR_2 + 1 + uVar1 & 0xff) - uVar1;
    *VAR_1 = *(FillArray + VAR_2) + *VAR_1;
    uVar1 = (*VAR_1 >> 0x1f) >> 0x18;
    *VAR_1 = (*VAR_1 + uVar1 & 0xff) - uVar1;
    swapVal(*(FillArray + VAR_2), *(FillArray + VAR_1));
    return *(FillArray (*(FillArray + VAR_1) + *(FillArray + VAR_2)));
}

void procSwap(int64_t arg1, int64_t arg2)
{
    ...
    *VAR_2 = 0;
    while (*VAR_2 < 0x100) {
        iVar2 = *(FillArray + VAR_2) + *VAR_1 + *(arg1 + *VAR_2 % arg2);
        uVar1 = (iVar2 >> 0x1f) >> 0x18;
        *VAR_1 = (iVar2 + uVar1 & 0xff) - uVar1;
        swapVal(*(FillArray + VAR_2), *(FillArray + *VAR_1));
        *VAR_2 = *VAR_2 + 1;
    }
    *VAR_1 = 0;
    *VAR_2 = 0;
    return;
}

undefined8 main(undefined8 argc, char **argv)
{
    int64_t in_FS_OFFSET;
    char **var_40h;
    int64_t var_34h;
    uint8_t buf;
    uint8_t ptr;
    uint8_t var_25h;
    int32_t nbytes;
    undefined8 var_20h;
    uint32_t fd;
    uint32_t var_14h;
    int64_t var_10h;
    int64_t canary;
    
    canary = *(int64_t *)(in_FS_OFFSET + 0x28);
    var_20h._0_4_ = 1;
    var_20h._4_4_ = sym.imp.open(0xce2, 0);
    if (var_20h._4_4_ == -1) {
    // WARNING: Subroutine does not return
        sym.imp.exit(0xffffffff);
    }
    fd = sym.imp.open(0xceb, 0x41);
    if (fd == 0xffffffff) {
    // WARNING: Subroutine does not return
        sym.imp.exit(0xffffffff);
    }
    randomVal(var_10h);
    var_14h = 0x20;
    fillArr();
    procSwap(*(int64_t *)0x202010, 0x10);// 0x202010 -> "rhcmem__c\xadem__\xdaC"
    J = 0;
    while (J < (int32_t)var_14h) {
        var_25h = getValFromArr();
        ptr = *(RandArr + J) ^ var_25h;
        sym.imp.write(FlagEnc, &ptr, 1);
        J = J + 1;
    }
    fillArr();
    procSwap(RandArr, var_14h);
    while( true ) {
        Flag._0_4_ = sym.imp.read(Flag._4_4_, &buf, 1, &buf);
        if ((int32_t)Flag < 1) break;
        var_25h = getValFromArr();
        ptr = buf ^ var_25h;
        sym.imp.write(FlagEnc, &ptr, 1, &ptr);
    }
    sym.imp.close(Flag._4_4_);
    sym.imp.close(FlagEnc);
    if (canary != *(int64_t *)(in_FS_OFFSET + 0x28)) {
    // WARNING: Subroutine does not return
        sym.imp.__stack_chk_fail();
    }
    return 1;
}