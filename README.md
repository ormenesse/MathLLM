# MathLLM

Even with a small model and training set, we can it works!


```
device(type='mps')
The model has 25,373,847 trainable parameters
(torch.Size([60, 1480806]),
 torch.Size([1480806]),
 torch.Size([60, 370017]),
 torch.Size([370017]))
succeeding standpoint 4 4 4 make 4 make make make make 4 understand standpoint 3 4 understand 4 understand 4 understand 4 4 4 <num> 4 4 make standpoint standpoint 3 standpoint make 4 4 standpoint make 3 make 4 understand standpoint standpoint standpoint make standpoint could 4 standpoint impression make standpoint 4 4 4 understand impression 4 4 3
Model Loaded Successfully!
Start training 0
Validating... 0
Epoch: 01 | Time: 77m 35s
	Train Loss: 30.172 | Train PPL: 12696148251230.764
	 Val. Loss: 34.744 |    Val. PPL: 1228270249703555.000
Testing:

	 Query:
	PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD SOS can you solve this subsequent mathematical function :  ( <num> 7 </num> + <num> 5 </num> ) EOS SOS it strikes me as possible that the response is :  <num> 1 2

	 Answer:
	</num> EOS



Start training 1
Validating... 1
Epoch: 02 | Time: 79m 9s
	Train Loss: 30.226 | Train PPL: 13392793701646.754
	 Val. Loss: 34.009 |    Val. PPL: 588957441234806.625
Start training 2
Validating... 2
Epoch: 03 | Time: 81m 53s
	Train Loss: 30.826 | Train PPL: 24399221451482.246
	 Val. Loss: 63.522 |    Val. PPL: 3864388997450516340701921280.000
Start training 3
Validating... 3
Epoch: 04 | Time: 80m 0s
	Train Loss: 31.221 | Train PPL: 36250466100053.133
	 Val. Loss: 60.211 |    Val. PPL: 141039426508387122084315136.000
Start training 4
Validating... 4
Epoch: 05 | Time: 81m 6s
	Train Loss: 31.662 | Train PPL: 56316545497473.172
	 Val. Loss: 50.024 |    Val. PPL: 5313136395573377630208.000
Start training 5
Validating... 5
Epoch: 06 | Time: 81m 31s
	Train Loss: 32.157 | Train PPL: 92342160891502.359
	 Val. Loss: 40.709 |    Val. PPL: 478318182623995584.000
Start training 6
Validating... 6
Epoch: 07 | Time: 80m 41s
	Train Loss: 31.743 | Train PPL: 61037579671273.758
	 Val. Loss: 38.085 |    Val. PPL: 34679764750380032.000
Start training 7
Validating... 7
Epoch: 08 | Time: 495m 17s
	Train Loss: 32.866 | Train PPL: 187716918151975.438
	 Val. Loss: 32.540 |    Val. PPL: 135448437129564.500
Start training 8
Validating... 8
Epoch: 09 | Time: 288m 8s
	Train Loss: 33.262 | Train PPL: 278836316788401.031
	 Val. Loss: 33.197 |    Val. PPL: 261444742797584.781
Start training 9
Validating... 9
Epoch: 10 | Time: 82m 4s
	Train Loss: 33.506 | Train PPL: 355914125511254.125
	 Val. Loss: 72.480 |    Val. PPL: 30036779881560540942067033964544.000
Start training 10
Validating... 10
Epoch: 11 | Time: 83m 16s
	Train Loss: 34.075 | Train PPL: 629040072336516.250
	 Val. Loss: 44.810 |    Val. PPL: 28878673096682766336.000
Testing:

	 Query:
	PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD PAD SOS hey ,  would you calculate the subsequent formula :  <num> 3 </num> + <num> 2 </num> EOS SOS

	 Answer:
	<num> 5 </num> EOS



Start training 11
Validating... 11
Epoch: 12 | Time: 83m 50s
	Train Loss: 33.662 | Train PPL: 415971062824650.188
	 Val. Loss: 49.018 |    Val. PPL: 1941550640344109678592.000
Start training 12
Validating... 12
Epoch: 13 | Time: 87m 2s
	Train Loss: 33.648 | Train PPL: 410167397080081.188
	 Val. Loss: 52.359 |    Val. PPL: 54833353538467098787840.000
Start training 13
Validating... 13
Epoch: 14 | Time: 86m 55s
	Train Loss: 34.443 | Train PPL: 908627280620166.750
	 Val. Loss: 52.082 |    Val. PPL: 41580518605405271621632.000
Start training 14
Validating... 14
Epoch: 15 | Time: 87m 51s
	Train Loss: 34.905 | Train PPL: 1441978385866249.750
	 Val. Loss: 51.852 |    Val. PPL: 33052697132174193721344.000
Start training 15
Validating... 15
Epoch: 16 | Time: 80m 25s
	Train Loss: 34.664 | Train PPL: 1132950338729782.500
	 Val. Loss: 55.987 |    Val. PPL: 2064457253091850498080768.000
Start training 16
Validating... 16
Epoch: 17 | Time: 86m 1s
	Train Loss: 35.464 | Train PPL: 2522079256162210.000
	 Val. Loss: 72.312 |    Val. PPL: 25393409013094371993326320615424.000
Start training 17
Validating... 17
Epoch: 18 | Time: 83m 6s
	Train Loss: 36.003 | Train PPL: 4325547031614765.000
	 Val. Loss: 46.805 |    Val. PPL: 212486565353291874304.000
```