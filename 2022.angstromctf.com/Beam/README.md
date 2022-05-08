#### Challenge:

Elixir needs more appreciation. Here's a [beam file](./Elixir.Angstrom.CLI.beam ":ignore").

Connect to it at `nc challs.actf.co 31400`.

---

#### Solution:

- each `beam` file can be decompiled via appropriate version of it's run-time environment
```bash
docker run --rm -it -v $(pwd):/work -w /work erlang io:format("~p~n",[beam_disasm:file("Elixir.Angstrom.CLI.beam")])
```

- inspection of the decompiled code reveals that to retrieve the flag we need supply correct input that is static
- in function `check` we see that we are comparing against `gjsfxpslt` string and out `input` is altered via function `-check/0-fun-0-` so that each `char` is incremented by `1`

```elixir
    {function,check,0,9,
         [{line,1},
          {label,8},
          {func_info,{atom,'Elixir.Angstrom.CLI'},{atom,check},0},
          {label,9},
          {allocate,0,0},
          {line,2},
          {call,0,{'Elixir.Angstrom.CLI',get_input,0}},
          {line,3},
          {call_ext,1,{extfunc,'Elixir.String',to_charlist,1}},
          {test_heap,{alloc,[{words,0},{floats,0},{funs,1}]},1},
          {make_fun3,
              {'Elixir.Angstrom.CLI','-check/0-fun-0-',1},
              0,98792139,
              {x,1},
              {list,[]}},
          {line,4},
          {call_ext,2,{extfunc,'Elixir.Enum',map,2}},
          {test,is_eq_exact,{f,10},[{x,0},{literal,"gjsfxpslt"}]},
          {call_last,0,{'Elixir.Angstrom.CLI',get_flag,0},0},
          {label,10}, 
          {move,{literal,<<"Sorry, no flag for you">>},{x,0}},
          {line,5},
          {call_ext_last,1,{extfunc,'Elixir.IO',puts,1},0}]},
     {function,'-check/0-fun-0-',1,24,
         [{line,4},
          {label,23},
          {func_info,{atom,'Elixir.Angstrom.CLI'},{atom,'-check/0-fun-0-'},1},
          {label,24},
          {gc_bif,'+',{f,0},1,[{x,0},{integer,1}],{x,0}},
          return]}]}
```

```bash
python3 -c "print(''.join([chr(ord(x)-1) for x in 'tlspxfsjg'])[::-1])" | nc challs.actf.co 31400
```

---

<details><summary>FLAG:</summary>

```
actf{elixir_is_awesome}
```

</details>
<br/>
