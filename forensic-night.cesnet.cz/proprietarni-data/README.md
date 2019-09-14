#### Challenge:

Analyzujte datový soubor proprietární aplikace, kterou už nelze sehnat. Porozumět způsobu ukládání dat by se docela hodilo, ať už je v souboru uloženo cokoliv. [file.dat.gz](./file.dat.gz ':ignore')

---

#### Solution:

```sql
select Char from data where PartOf = (select ID from ids where Description = 'flag') order by Position;
```

---

<details><summary>FLAG:</summary>

```
flag{Marissa_Mayer-0649}
```

</details>
